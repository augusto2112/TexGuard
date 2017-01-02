
from PySide.QtGui import *
from PySide.QtCore import *

from bin.model.pedidoTeflonModel import PedidoTeflonTableModel
from bin.widget.abstractPedidoWidget import AbstractPedidoWidget
from bin.view.pedidoTeflonTableView import PedidoTeflonTableView


class PedidoTeflonWidget(AbstractPedidoWidget):
    def __init__(self, parent=None):
        AbstractPedidoWidget.__init__(self, parent)
        self._model_class = PedidoTeflonTableModel
        self.set_table_view(PedidoTeflonTableView)

    def excluir_pedido(self, cod_pedido):
        self.model.sourceModel().excluir_pedido(cod_pedido)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = PedidoTeflonWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())