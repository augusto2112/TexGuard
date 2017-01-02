
from PySide.QtGui import *

from bin.model.pedidoPLTableModel import PedidoPLTableModel
from bin.widget.abstractPedidoWidget import AbstractPedidoWidget
from bin.view.pedidoPLTableView import PedidoPLTableView


class PedidoPLWidget(AbstractPedidoWidget):
    def __init__(self, parent=None):
        AbstractPedidoWidget.__init__(self, parent)
        self._model_class = PedidoPLTableModel
        self.set_table_view(PedidoPLTableView)

if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = PedidoPLWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())
