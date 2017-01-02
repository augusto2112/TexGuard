from datetime import date

from PySide.QtCore import *
from PySide.QtGui import *
from sqlalchemy.orm import contains_eager, joinedload

import bin.db.constants
from bin.db.comissao import Comissao
from bin.db.pedido_prima_linea import PedidoPrimaLinea
from bin.db.pedido_teflon import PedidoTeflon
from bin.db.session import Session
from bin.db.vendedor import Vendedor
from bin.model.selecaoProdutoTableModel import SelecaoProdutoTableModel
from bin.ui.cadastro_pedido_atrelado_ui import Ui_CadastroPedidoAtreladoDialog
from bin.widget.cadastroPagamentoDialog import CadastroPagamentoDialog

TIPO_VENDA = {"Vendeu na Loja": 1,
              "Cliente ligou e comprou": 2,
              "Vendeu no pós-venda": 3}


class CadastroPedidoAtreladoWidget(Ui_CadastroPedidoAtreladoDialog, QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = self.setupUi(self)
        self.pesquisarPushButton.clicked.connect(self.pesquisar_pedido)

        def enter_pressed():
            self.pesquisarPushButton.animateClick()

        QShortcut(QKeySequence(Qt.Key_Enter), self, enter_pressed)

        self.lojaComboBox.addItems(["Não Disponível"] + bin.db.constants.get_lojas())
        self.vendedorComboBox.addItems(bin.db.constants.get_vendedores())
        self.comissaoVendedorComboBox.addItems(["Não Disponível"] + bin.db.constants.get_vendedores())
        self.comissaoDecoradorComboBox.addItems(["Não Disponível"] + bin.db.constants.get_vendedores())
        self.comissaoGerenteComboBox.addItems(["Não Disponível"] + bin.db.constants.get_gerentes())
        self.tipoVendaComboBox.addItems(sorted(list(TIPO_VENDA.keys())))

        self.dataVendaPLDateEdit.setDate(date.today())
        self.dataVendaDateEdit.setDate(date.today())
        self.pedido_teflon = None
        self.cadastrarPushButton.clicked.connect(self.cadastrar_pedido)
        self.tableView.setSortingEnabled(True)
        self.model = QSortFilterProxyModel()
        self.tableView.setModel(self.model)

    def pesquisar_pedido(self):
        session = Session()
        cod_pedido = self.pedidoPLLineEdit.text()
        query = session.query(PedidoPrimaLinea)\
                .join(PedidoPrimaLinea.cliente)\
                .join(PedidoPrimaLinea.vendedor)\
                .options(joinedload("cliente"),
                         joinedload("vendedor"))\
                .filter(PedidoPrimaLinea.cod_pedido == cod_pedido)
        pedido_pl = query.all()
        session.close()

        if len(pedido_pl) == 1:
            pedido_pl = pedido_pl[0]
            self.clientePLLineEdit.setText(pedido_pl.cliente.nome)
            self.vendedorPLLineEdit.setText(pedido_pl.vendedor.nome_vendedor)
            self.lojaPLLineEdit.setText(pedido_pl.cod_loja)
            self.dataVendaPLDateEdit.setDate(pedido_pl.data_pedido)
            self.pedido_teflon = PedidoTeflon(cod_pedido_pl=pedido_pl.cod_pedido,
                                                                   cliente=pedido_pl.cliente,
                                                                   cod_endereco=pedido_pl.cod_endereco)
            self.comissaoVendedorComboBox.setCurrentIndex(self.comissaoVendedorComboBox.findText(
                                                          pedido_pl.vendedor.nome_vendedor))
            self.vendedorComboBox.setCurrentIndex(self.vendedorComboBox.findText(
                                                  pedido_pl.vendedor.nome_vendedor))
            loja_gerentes = bin.db.constants.get_loja_gerentes()
            self.comissaoGerenteComboBox.setCurrentIndex(self.comissaoGerenteComboBox.findText(
                                                         bin.db.constants.get_loja_gerentes()[pedido_pl.cod_loja]))
            self.lojaComboBox.setCurrentIndex(self.lojaComboBox.findText(pedido_pl.cod_loja))
            self.dataVendaDateEdit.setDate(pedido_pl.data_pedido)
            self.tipoVendaComboBox.setCurrentIndex(1)
            model = SelecaoProdutoTableModel(self.pedido_teflon)
            self.model.setSourceModel(model)
            self.tableView.resizeColumnsToContents()

    def cadastrar_pedido(self):
        def cadastrar():
            self.clear_fields()
            session = Session()
            session.add(self.pedido_teflon)
            session.commit()
            session.close()
            QMessageBox.information(self, "Confirmado", "Pedido Cadastrado!")
            self.clear_fields()

        model = self.model.sourceModel()
        confirmacao = QMessageBox.question(self, "Confirmação", "Tem certeza que deseja cadastrar esta venda?",
                                           QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if model and confirmacao == QMessageBox.Yes:
            aplicacoes = model.get_quantidade_novas_aplicacoes()
            VENDEDORES_DIC, GERENTES_DIC = bin.db.constants.get_vendedores_dic(), bin.db.constants.get_gerentes_dic()

            if self.valorTotalLineEdit.text() == '':
                QMessageBox.warning(self, "Preencha os campos requeridos",
                                        'O campo "Valor Total" é obrigatório')
            elif aplicacoes == 0:
                QMessageBox.warning(self, "Cadastre aplicações",
                                        'Marque as novas aplicações feitas com essa venda')
            else:
                self.pedido_teflon.valor = float(self.valorTotalLineEdit.text())
                self.pedido_teflon.cod_vendedor = VENDEDORES_DIC[self.vendedorComboBox.currentText()]
                self.pedido_teflon.cod_loja = self.lojaComboBox.currentText()
                self.pedido_teflon.tipo_venda = TIPO_VENDA[self.tipoVendaComboBox.currentText()]
                self.pedido_teflon.data_pedido = self.dataVendaDateEdit.date().toPython()
                self.pedido_teflon.data_cadastro = date.today()
                if self.comissaoVendedorComboBox.currentIndex() > 0:
                    valor_comissao = self.pedido_teflon.valor * 0.25
                    if self.comissaoDecoradorComboBox.currentIndex() > 0:
                        valor_comissao /= 2
                    comissao = Comissao(
                        cod_vendedor=VENDEDORES_DIC[self.comissaoVendedorComboBox.currentText()],
                        pedido_teflon=self.pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )
                if self.comissaoDecoradorComboBox.currentIndex() > 0:
                    valor_comissao = self.pedido_teflon.valor * 0.125
                    comissao = Comissao(
                        cod_vendedor=VENDEDORES_DIC[self.comissaoDecoradorComboBox.currentText()],
                        pedido_teflon=self.pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )
                if self.comissaoGerenteComboBox.currentIndex() > 0:
                    valor_comissao = self.pedido_teflon.valor * 0.05
                    comissao = Comissao(
                        cod_vendedor=GERENTES_DIC[self.comissaoGerenteComboBox.currentText()],
                        pedido_teflon=self.pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )

                self.pagamento_dialog = CadastroPagamentoDialog(self.pedido_teflon, self)
                self.pagamento_dialog.setModal(True)
                self.pagamento_dialog.show()
                self.pagamento_dialog.accepted.connect(cadastrar)

    def clear_fields(self):
        for widget in self.children():
            if type(widget) is QLineEdit:
                widget.clear()
            elif type(widget) is QComboBox:
                widget.setCurrentIndex(0)
            elif type(widget) is QDateEdit:
                widget.setDate(date.today())
        self.model = QSortFilterProxyModel()
        self.tableView.setModel(self.model)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = CadastroPedidoAtreladoWidget()
    dialog.showMaximized()
    sys.exit(app.exec_())
