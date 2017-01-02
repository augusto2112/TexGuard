
from PySide.QtGui import *
from PySide.QtCore import *

import bin.db.constants
from bin.model.comissaoTableModel import ComissaoTableModel
from bin.ui.comissao_ui import Ui_ComissaoWidget
from bin.widget.abstractWidget import AbstractWidget
from bin.view.comissaoTableView import ComissaoTableView

from bin.sortFilterProxyModel.comissaoSortFilterProxyModel import ComissaoSortFilterProxyModel

class ComissaoWidget(Ui_ComissaoWidget,
                     AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = Ui_ComissaoWidget.setupUi(self, self)

        self.pesquisarPushButton.clicked.connect(self.set_model)
        self.aplicarPushButton.clicked.connect(self.commit)

        self.lojaComboBox.addItems(["Todas"] + bin.db.constants.get_lojas())

        self.dataInicialDateEdit.setDate(QDate.currentDate())
        self.dataFinalDateEdit.setDate(QDate.currentDate())

        self.set_table_view(ComissaoTableView)
        self.set_proxy_model()

    def set_model(self):
        vendedor = pedido = data_inicial = data_final = loja = None

        if self.vendedorCheckBox.isChecked():
            vendedor = self.vendedorLineEdit.text()
        if self.pedidoCheckBox.isChecked():
            pedido = self.pedidoLineEdit.text()
        if self.dataCheckBox.isChecked():
            data_inicial = self.dataInicialDateEdit.date().toPython()
            data_final = self.dataFinalDateEdit.date().toPython()
        if self.lojaCheckBox.isChecked():
            loja = self.lojaComboBox.currentText()

        raw_model = ComissaoTableModel(vendedor, pedido, data_inicial, data_final, loja)
        self.model.setSourceModel(raw_model)

    def set_proxy_model(self):
        self.tableView.setSortingEnabled(True)
        self.model = ComissaoSortFilterProxyModel()
        self.tableView.setModel(self.model)

    def commit(self):
        confirmacao = QMessageBox.question(self,
                                           "Confirmação", "Tem certeza que deseja aplicar as alterações?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if self.model.sourceModel() and confirmacao == QMessageBox.Yes:
            self.model.sourceModel().commit()
            self.set_model()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = ComissaoWidget()
    a.show()
    a.setFocus()
    sys.exit(app.exec_())