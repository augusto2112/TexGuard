
from datetime import date

import bin.ui.pedidos_ui
import bin.db.constants
import bin.widget.abstractWidget

from bin.ui.pedidos_ui import Ui_Pedidos
from bin.widget.abstractWidget import AbstractWidget

from bin.sortFilterProxyModel.pedidoSortFilterProxyModel import PedidoSortFilterProxyModel


class AbstractPedidoWidget(Ui_Pedidos, AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = Ui_Pedidos.setupUi(self, self)
        self._model_class = None #  Set model_class on subclasses
        self.lojaComboBox.addItems(["Todas"] + bin.db.constants.get_lojas())

        self.buscarPushButton.clicked.connect(self.set_model)

        self.dataInicialDateEdit.setDate(date.today())
        self.dataFinalDateEdit.setDate(date.today())
        self.set_proxy_model()

    def set_model(self):
        initial_date = final_date = loja = vendedor = \
            cliente = pedido = endereco = None

        if self.dataInicialCheckBox.isChecked():
            initial_date = self.dataInicialDateEdit.date().toPython()
        if self.dataFinalCheckBox.isChecked():
            final_date = self.dataFinalDateEdit.date().toPython()
        if self.lojaComboBox.currentIndex() > 0:
            loja = self.lojaComboBox.currentText()
        if self.vendedorCheckBox.isChecked():
            vendedor = self.vendedorLineEdit.text()
        if self.clienteCheckBox.isChecked():
            cliente = self.clienteLineEdit.text()
        if self.pedidoCheckBox.isChecked():
            pedido = self.pedidoLineEdit.text()
        if self.enderecoCheckBox.isChecked():
            endereco = self.enderecoLineEdit.text()
            print(pedido)

        raw_model = self._model_class(initial_date, final_date, loja, vendedor, cliente, pedido, endereco)
        self.model.setSourceModel(raw_model)
        self.tableView.resizeColumnsToContents()

    def set_proxy_model(self):
        self.tableView.setSortingEnabled(True)
        self.model = PedidoSortFilterProxyModel()
        self.tableView.setModel(self.model)
