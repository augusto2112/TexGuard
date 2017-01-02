
from PySide.QtGui import *

import bin.view.abstractTableView


class ClienteTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.enderecoWidget
        import bin.widget.pedidoTeflonWidget
        import bin.widget.pedidoPLWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        endereco_action = QAction("Ver Endereços", self)
        endereco_action.triggered.connect(self.abrir_endereco_nome)
        self.menu.addAction(endereco_action)

        venda_teflon_action = QAction("Ver Vendas de Teflon", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido_teflon)
        self.menu.addAction(venda_teflon_action)

        venda_pl_action = QAction("Ver Vendas da Prima Linea", self)
        venda_pl_action.triggered.connect(self.abrir_pedido_pl)
        self.menu.addAction(venda_pl_action)

    def abrir_endereco_nome(self):
        self.set_current_subview(bin.widget.enderecoWidget.EnderecoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_endereco_nome(self, 1)

    def abrir_pedido_teflon(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_cliente(self, 1)

    def abrir_pedido_pl(self):
        self.set_current_subview(bin.widget.pedidoPLWidget.PedidoPLWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_cliente(self, 1)
