
from PySide.QtGui import *

import bin.view.abstractTableView


class ComissaoTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.enderecoWidget
        import bin.widget.pedidoTeflonWidget
        import bin.widget.pedidoPLWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        vendedor_teflon_action = QAction("Ver vendas de teflon deste vendedor", self)
        vendedor_teflon_action.triggered.connect(self.abrir_pedido_teflon_vendedor)
        self.menu.addAction(vendedor_teflon_action)

        venda_pl_action = QAction("Ver vendas da Prima Linea deste vendedor", self)
        venda_pl_action.triggered.connect(self.abrir_pedido_pl_vendedor)
        self.menu.addAction(venda_pl_action)

        venda_teflon_action = QAction("Ver Esta Venda de Teflon", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido)
        self.menu.addAction(venda_teflon_action)

    def abrir_pedido_teflon_vendedor(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_vendedor(self, 0)

    def abrir_pedido_pl_vendedor(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_vendedor(self, 0)

    def abrir_pedido(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 1)

