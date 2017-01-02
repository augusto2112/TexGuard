
from datetime import date
from decimal import Decimal

from PySide.QtGui import *
from sqlalchemy.orm import contains_eager, joinedload

from bin.db.loja import Loja
from bin.db.vendedor import Vendedor
from bin.db.comissao import Comissao
from bin.db.pedido_teflon import PedidoTeflon
from bin.ui.selecao_impressao_ui import Ui_SelecaoImpressao

from bin.db.session import Session


class SelecaoImpressao(Ui_SelecaoImpressao, QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_SelecaoImpressao.setupUi(self, self)
        self.dateEdit.setDate(date.today())

        self.lojas_bh = {"02": self.loja02CheckBox, "04": self.loja04CheckBox,
                         "05": self.loja05CheckBox, "07": self.loja07CheckBox,
                         "08": self.loja08CheckBox, "11": self.loja11CheckBox,
                         "14": self.loja14CheckBox, "15": self.loja15CheckBox,}

        self.lojas_bsb = {"01": self.loja01CheckBox, "03": self.loja03CheckBox,
                          "06": self.loja06CheckBox, "09": self.loja09CheckBox,
                          "10": self.loja10CheckBox}

        self.buttonBox.accepted.connect(self.imprimir)


        for checkBox in self.lojas_bh.values():
            self.bhCheckBox.stateChanged.connect(checkBox.setChecked)
        for checkBox in self.lojas_bsb.values():
            self.bsbCheckBox.stateChanged.connect(checkBox.setChecked)

    def imprimir(self):
        selecionadas = [key for key, value in
                        dict(self.lojas_bh, **self.lojas_bsb).items()
                        if value.isChecked()]
        if self.bhCheckBox.isChecked():
            selecionadas.append("MG")
        if self.bsbCheckBox.isChecked():
            selecionadas.append("DF")
        if self.fabricaCheckBox.isChecked():
            selecionadas.append("00")
        selecionadas.sort()
        html = self.gerar_html(selecionadas)

        document = QTextDocument()
        document.setHtml(html)

        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            document.print_(printer)

    def gerar_html(self, lojas):
        session = Session()
        query = session.query(Loja) \
            .join(Loja.vendedores) \
            .join(Vendedor.comissoes) \
            .join(Comissao.pedido_teflon) \
            .options(contains_eager('vendedores'),
                     contains_eager('vendedores.comissoes'),
                     contains_eager('vendedores.comissoes.pedido_teflon'),
                     joinedload('vendedores.comissoes.pedido_teflon.pedido_pl')) \
            .filter(Loja.cod_loja.in_(lojas)) \
            .filter(Comissao.status_pagamento == 0) \
            .filter(PedidoTeflon.data_pedido <= self.dateEdit.date().toPython()) \

        table = """ <head>
                    <style>
                    table, th, td {
                        border: 1px solid black;
                    }
                    th, td {
                        padding: 5px;
                    }
                    </style>
                    </head>

                    <body>

                    <table border=0 align=center style="width:100%">
                    <tr>
                    <th>Cliente</th>
                    <th>Pedido</th>
                    <th>Data</th>
                    <th>Valor Total</th>
                    <th>Comissão</th>
                  </tr>"""
        table_gerente = """ <head>
                    <style>
                    table, th, td {
                        border: 1px solid black;
                    }
                    th, td {
                        padding: 5px;
                    }
                    </style>
                    </head>

                    <body>

                    <table border=0 align=center style="width:100%">
                    <tr>
                    <th>Vendedor</th>
                    <th>Pedido</th>
                    <th>Data</th>
                    <th>Valor Total</th>
                    <th>Comissão</th>
                  </tr>"""
        html = ""

        lojas = query.all()
        for loja in lojas:
            print(loja.vendedores)
            for vendedor in loja.vendedores:
                if vendedor.tipo_vendedor == 1 or vendedor.tipo_vendedor == 2:
                    print("usando gerente")
                    html += "<h1><center>Loja {}</center></h1><br>".format(loja.cod_loja)
                    html += "<h2><center>{}</center></h2><br>".format(vendedor.nome_vendedor)
                    html += table_gerente
                    total_pedidos, total_comissoes = 0, 0
                    for comissao in vendedor.comissoes:
                        total_pedidos += comissao.pedido_teflon.valor
                        total_comissoes += comissao.valor
                        if comissao.pedido_teflon.pedido_pl is None:
                            html += "<tr><th>{4}</th><th>{0}</th><th>{1}</th>" \
                                    "<th>{2}</th><th>{3}</th></tr>". \
                                format(comissao.pedido_teflon.cod_pedido,
                                       comissao.pedido_teflon.data_pedido.strftime("%d/%m/%y"),
                                       round(Decimal(comissao.pedido_teflon.valor), 2), round(Decimal(comissao.valor), 2),
                                       comissao.pedido_teflon.vendedor.nome_vendedor)
                        else:
                            html += "<tr><th>{4}</th><th>{0}</th><th>{1}</th>" \
                                    "<th>{2}</th><th>{3}</th></tr>". \
                                format(comissao.pedido_teflon.cod_pedido_pl,
                                       comissao.pedido_teflon.pedido_pl.data_pedido.strftime("%d/%m/%y"),
                                       round(Decimal(comissao.pedido_teflon.valor), 2), round(Decimal(comissao.valor), 2),
                                       comissao.pedido_teflon.vendedor.nome_vendedor)
                    html += "<tr><th></th><th></th><th></th>" \
                            "<th>{0}</th><th>{1}</th></tr>". \
                        format(round(Decimal(total_pedidos), 2), round(Decimal(total_comissoes), 2))
                    html += "</table>"
                    html += u'<br><br><br><br><br><p align="right">________________________________<br>'
                    html += "{0}</p><br><br>".format(vendedor.nome_vendedor)
                    if vendedor is not loja.vendedores[-1] or \
                            loja is not lojas[-1]:
                        html += "<div style=\"page-break-after:always\"></div>"
                else:
                    html += "<h1><center>Loja {}</center></h1><br>".format(loja.cod_loja)
                    html += "<h2><center>{}</center></h2><br>".format(vendedor.nome_vendedor)
                    html += table
                    total_pedidos, total_comissoes = 0, 0
                    for comissao in vendedor.comissoes:
                        print(comissao.cod_pedido_teflon)
                        total_pedidos += comissao.pedido_teflon.valor
                        total_comissoes += comissao.valor
                        if comissao.pedido_teflon.pedido_pl is None:
                            html += "<tr><th>{4}</th><th>{0}</th><th>{1}</th>" \
                                    "<th>{2}</th><th>{3}</th></tr>". \
                                format(comissao.pedido_teflon.cod_pedido,
                                       comissao.pedido_teflon.data_pedido.strftime("%d/%m/%y"),
                                       round(Decimal(comissao.pedido_teflon.valor), 2), round(Decimal(comissao.valor), 2),
                                       comissao.pedido_teflon.cliente.nome)
                        else:
                            html += "<tr><th>{4}</th><th>{0}</th><th>{1}</th>" \
                                    "<th>{2}</th><th>{3}</th></tr>". \
                                format(comissao.pedido_teflon.cod_pedido_pl,
                                       comissao.pedido_teflon.pedido_pl.data_pedido.strftime("%d/%m/%y"),
                                       round(Decimal(comissao.pedido_teflon.valor), 2), round(Decimal(comissao.valor), 2),
                                       comissao.pedido_teflon.cliente.nome)
                    html += "<tr><th></th><th></th><th></th>" \
                            "<th>{0}</th><th>{1}</th></tr>". \
                        format(round(Decimal(total_pedidos), 2), round(Decimal(total_comissoes), 2))
                    html += "</table>"
                    html += u'<br><br><br><br><br><p align="right">________________________________<br>'
                    html += "{0}</p><br><br>".format(vendedor.nome_vendedor)
                    if vendedor is not loja.vendedores[-1] or \
                            loja is not lojas[-1]:
                        html += "<div style=\"page-break-after:always\"></div>"
        session.close()
        return html

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    a = SelecaoImpressao()
    a.show()
    sys.exit(app.exec_())