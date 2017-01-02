
from PySide.QtGui import *

import bin.view.abstractTableView


class AplicacaoTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.pedidoTeflonWidget
        import bin.widget.pedidoPLWidget
        import bin.widget.produtoWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        venda_teflon_action = QAction("Ver Venda de Teflon", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido_teflon)
        self.menu.addAction(venda_teflon_action)

        venda_pl_action = QAction("Ver Venda da Prima Linea", self)
        venda_pl_action.triggered.connect(self.abrir_pedido_pl)
        self.menu.addAction(venda_pl_action)

        produto_action = QAction("Ver produto", self)
        produto_action.triggered.connect(self.abrir_produto)
        self.menu.addAction(produto_action)

    def abrir_pedido_teflon(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 1)

    def abrir_pedido_pl(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 2)

    def abrir_produto(self):
        self.set_current_subview(bin.widget.produtoWidget.ProdutoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_produto(self, 3)