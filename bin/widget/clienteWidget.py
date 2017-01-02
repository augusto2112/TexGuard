
from PySide.QtGui import *

from bin.model.clienteTableModel import ClienteTableModel
from bin.view.clienteTableView import ClienteTableView
from bin.ui.cliente_ui import Ui_ClienteWidget
from bin.widget.abstractWidget import AbstractWidget


class ClienteWidget(Ui_ClienteWidget, AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.pesquisarPushButton.clicked.connect(self.set_model)

        self.set_table_view(ClienteTableView)
        self.set_proxy_model()

    def set_model(self):
        if self.nomeRadioButton.isChecked():
            model = ClienteTableModel(nome=self.lineEdit.text())
        elif self.codigoRadioButton.isChecked():
            model = ClienteTableModel(codigo=self.lineEdit.text())
        self.model.setSourceModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = ClienteWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())
