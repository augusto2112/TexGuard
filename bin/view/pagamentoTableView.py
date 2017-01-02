
from PySide.QtGui import *

import bin.view.abstractTableView


class PagamentoTableView(bin.view.abstractTableView.AbstractTableView):
    def __init__(self, *args, **kwargs):
        import bin.widget.pedidoTeflonWidget
        import bin.widget.clienteWidget

        bin.view.abstractTableView.AbstractTableView.__init__(self, *args, **kwargs)

        venda_teflon_action = QAction("Ver Venda de Teflon deste pagamento", self)
        venda_teflon_action.triggered.connect(self.abrir_pedido_teflon)
        self.menu.addAction(venda_teflon_action)

        cliente_action = QAction("Ver este cliente", self)
        cliente_action.triggered.connect(self.abrir_cliente)
        self.menu.addAction(cliente_action)

    def abrir_pedido_teflon(self):
        self.set_current_subview(bin.widget.pedidoTeflonWidget.PedidoTeflonWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_pedido(self, 1)

    def abrir_cliente(self):
        self.set_current_subview(bin.widget.clienteWidget.ClienteWidget)
        bin.view.abstractTableView.AbstractTableView.abrir_cliente(self, 2)
