
from PySide.QtGui import *


import bin.view.abstractTableView


class PedidoTeflonTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.enderecoWidget
        import bin.widget.pedidoPLWidget
        import bin.widget.clienteWidget
        import bin.widget.comissaoWidget
        import bin.widget.pagamentoWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        endereco_action = QAction("Ver Endereços", self)
        endereco_action.triggered.connect(self.abrir_endereco)
        self.menu.addAction(endereco_action)

        venda_pl_action = QAction("Ver Venda Prima Linea", self)
        venda_pl_action.triggered.connect(self.abrir_pedido)
        self.menu.addAction(venda_pl_action)

        cliente_action = QAction("Ver Cliente", self)
        cliente_action.triggered.connect(self.abrir_cliente)
        self.menu.addAction(cliente_action)

        comissao_action = QAction("Ver Comissão Relacionada a este pedido", self)
        comissao_action.triggered.connect(self.abrir_comissao)
        self.menu.addAction(comissao_action)

        pagamento_action = QAction("Ver Pagamentos Relacionados a este pedido", self)
        pagamento_action.triggered.connect(self.abrir_pagamento)
        self.menu.addAction(pagamento_action)

        excluir_action = QAction("Excluir pedido", self)
        excluir_action.triggered.connect(self.excluir_pedido)

        self.menu.addAction(excluir_action)

    def abrir_endereco(self):
        self.set_current_subview(bin.widget.enderecoWidget.EnderecoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_endereco_nome(self, 3)

    def abrir_pedido(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 2)

    def abrir_cliente(self):
        self.set_current_subview(bin.widget.clienteWidget.ClienteWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_cliente(self, 3)

    def abrir_comissao(self):
        self.set_current_subview(bin.widget.comissaoWidget.ComissaoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_comissao(self, 0)

    def abrir_pagamento(self):
        self.set_current_subview(bin.widget.pagamentoWidget.PagamentoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pagamento(self, 0)

    def excluir_pedido(self):
        confirmacao = QMessageBox.question(self, "Confirmação", "Este processo é IRREVERSIVEL. Tem certeza que deseja"
                                                                "excluir este pedido e todas as comissoes e pagamentos"
                                                                "ligadas a ela?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirmacao == QMessageBox.Yes:
            index = self.model().index(self.rowAt(self.y), 0)
            self.parentWidget().excluir_pedido(index.data())
        