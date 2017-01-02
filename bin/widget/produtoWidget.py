
from PySide.QtGui import *

from bin.model.produtoTableModel import ProdutoTableModel
from bin.ui.produto_ui import Ui_ProdutoWidget
from bin.widget.abstractWidget import AbstractWidget
from bin.view.produtoTableView import ProdutoTableView


class ProdutoWidget(Ui_ProdutoWidget, AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.pesquisarPushButton.clicked.connect(self.set_model)

        self.vendeuTeflonComboBoxMapping = {"Não": "N", "Sim": "S"}
        self.vendeuTeflonComboBox.addItems(["Não", "Sim"])

        self.set_table_view(ProdutoTableView)
        self.set_proxy_model()

    def set_model(self):
        pedido_pl = cod_produto = vendeu_teflon = None

        if self.pedidoPLCheckBox.isChecked():
            pedido_pl = self.pedidoLineEdit.text()
        if self.codProdutoCheckBox.isChecked():
            cod_produto = self.codProdutoLineEdit.text()
        if self.vendeuTeflonCheckBox.isChecked():
            vendeu_teflon = self.vendeuTeflonComboBoxMapping[self.vendeuTeflonComboBox.currentText()]

        model = ProdutoTableModel(pedido_pl, cod_produto, vendeu_teflon)

        self.model.setSourceModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = ProdutoWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())
