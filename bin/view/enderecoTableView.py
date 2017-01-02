
from PySide.QtGui import *

import bin.view.abstractTableView


class EnderecoTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.enderecoWidget
        import bin.widget.pedidoTeflonWidget
        import bin.widget.pedidoPLWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        venda_teflon_action = QAction("Ver Vendas de Teflon neste endereço", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido_teflon_endereco)
        self.menu.addAction(venda_teflon_action)

        venda_pl_action = QAction("Ver Vendas da Prima Linea neste endereço", self)
        venda_pl_action.triggered.connect(self.abrir_pedido_pl_endereco)
        self.menu.addAction(venda_pl_action)

    def abrir_pedido_teflon_endereco(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_endereco(self, 0)

    def abrir_pedido_pl_endereco(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_endereco(self, 0)