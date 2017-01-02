from datetime import date

from PySide.QtCore import *
from PySide.QtGui import *
from sqlalchemy.orm import contains_eager, joinedload

import bin.db.constants

from bin.db.session import Session

from bin.db.pedido_teflon import PedidoTeflon
from bin.db.cliente import Cliente
from bin.db.comissao import Comissao
from bin.db.endereco import Endereco

from bin.ui.cadastro_pedido_independente_ui import Ui_CadastroPedidoIndependenteDialog

from bin.widget.clienteWidget import ClienteWidget
from bin.widget.cadastroPagamentoDialog import CadastroPagamentoDialog
from bin.widget.cadastroClienteWidget import CadastroClienteDialog

TIPO_VENDA = {"Vendeu na Loja": 1,
              "Cliente ligou e comprou": 2,
              "Vendeu no pós-venda": 3}


class CadastroPedidoIndependenteWidget(Ui_CadastroPedidoIndependenteDialog, QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = self.setupUi(self)
        self.selecionarClientePushButton.clicked.connect(self.selecionar_cliente)
        self.cadastrarClientePushButton.clicked.connect(self.cadastrar_cliente)

        self.lojaComboBox.addItems(bin.db.constants.get_lojas())
        self.vendedorComboBox.addItems(bin.db.constants.get_vendedores())
        self.comissaoVendedorComboBox.addItems(["Não Disponível"] + bin.db.constants.get_vendedores())
        self.comissaoDecoradorComboBox.addItems(["Não Disponível"] + bin.db.constants.get_vendedores())
        self.comissaoGerenteComboBox.addItems(["Não Disponível"] + bin.db.constants.get_gerentes())
        self.tipoVendaComboBox.addItems(sorted(list(TIPO_VENDA.keys())))

        self.dataVendaDateEdit.setDate(date.today())
        self.cliente = None
        self.cadastrarPushButton.clicked.connect(self.cadastrar_pedido)

    def selecionar_cliente(self):
        def cliente_selecionado(index):
            cod_cliente = cliente_widget.model.data(cliente_widget.model.index(index.row(), 0))
            cliente_widget.close()

            session = Session()
            query = session.query(Cliente)\
                .options(joinedload(Cliente.enderecos))\
                .filter(Cliente.cod_cliente == cod_cliente)
            self.cliente = query.one()
            session.close()

            self.nomeClienteLineEdit.setText(self.cliente.nome)

        cliente_widget = ClienteWidget()
        cliente_widget.setWindowModality(Qt.ApplicationModal)
        cliente_widget.show()
        cliente_widget.tableView.doubleClicked.connect(cliente_selecionado)

    def cadastrar_cliente(self):
        def cadastrado():
            self.cliente = cadastro_cliente_dialog.cliente
            self.nomeClienteLineEdit.setText(self.cliente.nome)

        cadastro_cliente_dialog = CadastroClienteDialog(self)
        cadastro_cliente_dialog.setModal(True)
        cadastro_cliente_dialog.accepted.connect(cadastrado)
        cadastro_cliente_dialog.show()

    def cadastrar_pedido(self):
        def cadastrar():
            session = Session()
            session.add(pedido_teflon)
            session.commit()
            session.close()
            QMessageBox.information(self, "Confirmado", "Pedido Cadastrado!")
            self.cliente = None
            self.nomeClienteLineEdit.clear()

        confirmacao = QMessageBox.question(self, "Confirmação", "Tem certeza que deseja cadastrar esta venda?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirmacao == QMessageBox.Yes:
            VENDEDORES_DIC, GERENTES_DIC = bin.db.constants.get_vendedores_dic(), bin.db.constants.get_gerentes_dic()

            if self.valorTotalLineEdit.text() == '':
                QMessageBox.warning(self, "Preencha os campos requeridos",
                                    'O campo "Valor Total" é obrigatório')
            elif self.cliente is None:
                QMessageBox.warning(self, "Selecione o cliente",
                                    'Selecione o cliente')
            else:
                pedido_teflon = PedidoTeflon()
                pedido_teflon.cliente = self.cliente

                if pedido_teflon.cliente.enderecos:
                    pedido_teflon.endereco = pedido_teflon.cliente.enderecos[0]
                else:
                    session = Session()
                    query = session.query(Endereco).filter(Endereco.cod_endereco == 1)
                    pedido_teflon.endereco = query.one()
                    session.close()

                pedido_teflon.valor = float(self.valorTotalLineEdit.text())
                pedido_teflon.cod_vendedor = VENDEDORES_DIC[self.vendedorComboBox.currentText()]
                pedido_teflon.cod_loja = self.lojaComboBox.currentText()
                pedido_teflon.tipo_venda = TIPO_VENDA[self.tipoVendaComboBox.currentText()]
                pedido_teflon.data_pedido = self.dataVendaDateEdit.date().toPython()
                pedido_teflon.data_cadastro = date.today()
                if self.comissaoVendedorComboBox.currentIndex() > 0:
                    valor_comissao = pedido_teflon.valor * 0.25
                    if self.comissaoDecoradorComboBox.currentIndex() > 0:
                        valor_comissao /= 2
                    comissao = Comissao(
                        cod_vendedor=VENDEDORES_DIC[self.comissaoVendedorComboBox.currentText()],
                        pedido_teflon=pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )
                if self.comissaoDecoradorComboBox.currentIndex() > 0:
                    valor_comissao = pedido_teflon.valor * 0.125
                    comissao = Comissao(
                        cod_vendedor=VENDEDORES_DIC[self.comissaoDecoradorComboBox.currentText()],
                        pedido_teflon=pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )
                if self.comissaoGerenteComboBox.currentIndex() > 0:
                    valor_comissao = pedido_teflon.valor * 0.05
                    comissao = Comissao(
                        cod_vendedor=GERENTES_DIC[self.comissaoGerenteComboBox.currentText()],
                        pedido_teflon=pedido_teflon,
                        valor=valor_comissao,
                        data_pagamento=date.today(),
                        status_pagamento=0
                    )

                self.pagamento_dialog = CadastroPagamentoDialog(pedido_teflon, self)
                self.pagamento_dialog.setModal(True)
                self.pagamento_dialog.show()
                self.pagamento_dialog.accepted.connect(cadastrar)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = CadastroPedidoIndependenteWidget()
    dialog.showMaximized()
    sys.exit(app.exec_())
