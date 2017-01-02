
from PySide.QtGui import *

from bin.model.enderecoTableModel import EnderecoTableModel
from bin.ui.endereco_ui import Ui_EnderecoWidget
from bin.widget.abstractWidget import AbstractWidget

from bin.view.enderecoTableView import EnderecoTableView


class EnderecoWidget(Ui_EnderecoWidget,
                     AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = Ui_EnderecoWidget.setupUi(self, self)

        self.pesquisarPushButton.clicked.connect(self.set_model)

        self.set_proxy_model()
        self.set_table_view(EnderecoTableView)

    def set_model(self):
        if self.nomeClienteRadioButton.isChecked():
            model = EnderecoTableModel(nome_cliente=self.lineEdit.text())
        elif self.codigoClienteRadioButton.isChecked():
            model = EnderecoTableModel(cod_cliente=self.lineEdit.text())
        elif self.enderecoRadioButton.isChecked():
            model = EnderecoTableModel(endereco=self.lineEdit.text())
        elif self.cidadeRadioButton.isChecked():
            model = EnderecoTableModel(cidade=self.lineEdit.text())
        elif self.ufRadioButton.isChecked():
            model = EnderecoTableModel(uf=self.lineEdit.text())
        elif self.codEnderecoRadioButton.isChecked():
            model = EnderecoTableModel(cod_endereco=self.lineEdit.text())

        self.model.setSourceModel(model)
        self.tableView.resizeColumnsToContents()

if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = EnderecoWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())
