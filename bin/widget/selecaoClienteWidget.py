from PySide.QtCore import *
from PySide.QtGui import *

from bin.widget.clienteWidget import ClienteWidget


class SelecaoClienteWidget(ClienteWidget):
    def __init__(self, parent=None):
        ClienteWidget.__init__(self, parent)
        self.tableView.doubleClicked.connect(self.cliente_selecionado)

    def cliente_selecionado(self, index):
        self.cod_cliente = self.model.data(self.model.index(index.row(), 0))
        self.hide()

if __name__ == '__main__':
    import sys
    from bin.widget.mainWindowWidget import MainWindow
    app = QApplication(sys.argv)
    a = SelecaoClienteWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())