from PySide.QtGui import *

from bin.model.aplicacaoTableModel import AplicacaoTableModel
from bin.ui.aplicacao_ui import Ui_AplicacaoWidget
from bin.widget.abstractWidget import AbstractWidget
from bin.view.aplicacaoTableView import AplicacaoTableView


class AplicacaoWidget(Ui_AplicacaoWidget,AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.pesquisarPushButton.clicked.connect(self.set_model)

        self.set_table_view(AplicacaoTableView)
        self.set_proxy_model()

    def set_model(self):
        pedido_teflon = pedido_pl = cod_produto  = None

        if self.pedidoTeflonCheckBox.isChecked():
            pedido_teflon = self.pedidoTeflonLineEdit.text()
        if self.pedidoPLCheckBox.isChecked():
            pedido_pl = self.pedidoPLLineEdit.text()
        if self.codProdutoCheckBox.isChecked():
            cod_produto = self.codProdutoLineEdit.text()

        model = AplicacaoTableModel(pedido_teflon, pedido_pl, cod_produto)

        self.model.setSourceModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = AplicacaoWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())
