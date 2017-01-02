
from PySide.QtGui import *


import bin.view.abstractTableView


class ProdutoTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.aplicacaoWidget
        import bin.widget.pedidoPLWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        aplicacao_action = QAction("Ver Aplicacao de Teflon", self)
        aplicacao_action.triggered.connect(self.abrir_aplicacao)
        self.menu.addAction(aplicacao_action)

        venda_pl_action = QAction("Ver Venda da Prima Linea", self)
        venda_pl_action.triggered.connect(self.abrir_pedido_pl)
        self.menu.addAction(venda_pl_action)

    def abrir_pedido_pl(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 0)

    def abrir_aplicacao(self):
        self.set_current_subview(bin.widget.aplicacaoWidget.AplicacaoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_aplicacao(self, 2)