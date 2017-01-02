
from PySide.QtGui import *

import bin.view.abstractTableView


class PedidoPLTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.enderecoWidget
        import bin.widget.pedidoTeflonWidget
        import bin.widget.clienteWidget
        import bin.widget.pedidoDetalheWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        endereco_action = QAction("Ver Endereços", self)
        endereco_action.triggered.connect(self.abrir_endereco)
        self.menu.addAction(endereco_action)

        venda_teflon_action = QAction("Ver Venda de Teflon", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido)
        self.menu.addAction(venda_teflon_action)

        cliente_action = QAction("Ver cliente", self)
        cliente_action.triggered.connect(self.abrir_cliente)
        self.menu.addAction(cliente_action)

        detalhes_pedido_action = QAction("Ver detalhes do pedido", self)
        detalhes_pedido_action.triggered.connect(self.abrir_detalhes_pedido)
        self.menu.addAction(detalhes_pedido_action)

    def abrir_endereco(self):
        self.set_current_subview(bin.widget.enderecoWidget.EnderecoWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_endereco(self, 3)

    def abrir_pedido(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido_cliente(self, 2)

    def abrir_cliente(self):
        self.set_current_subview(bin.widget.clienteWidget.ClienteWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_cliente(self, 2)

    def abrir_detalhes_pedido(self):
        self.set_current_subview(bin.widget.pedidoDetalheWidget.PedidoDetalhe)
        bin.view.abstractTableView.AbstractTableView.abrir_detalhes_pedido(self, 0)
