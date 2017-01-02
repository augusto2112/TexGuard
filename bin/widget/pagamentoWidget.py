
from datetime import date

from PySide.QtGui import *

from bin.model.pagamentoTableModel import PagamentoTableModel
from bin.ui.pagamento_ui import Ui_PagamentoWidget
from bin.widget.abstractWidget import AbstractWidget
from bin.view.pagamentoTableView import PagamentoTableView


class PagamentoWidget(Ui_PagamentoWidget,
                      AbstractWidget):
    def __init__(self, parent=None):
        AbstractWidget.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.pesquisarPushButton.clicked.connect(self.set_model)

        for dateEdit in (self.dataPagoInicialDateEdit, self.dataPagoFinalDateEdit,
                         self.vencimentoDataInicialDateEdit, self.vencimentoDataFinalDateEdit):
            dateEdit.setDate(date.today())

        self.set_table_view(PagamentoTableView)
        self.set_proxy_model()

    def set_model(self):
        cod_pagamento = cod_pedido_teflon = cod_condicao_pagamento = pago = \
            conferido = vencimento_data_inicial = vencimento_data_final = \
            data_pago_data_inicial = data_pago_data_final = cliente = None

        if self.codigoPagamentoCheckBox.isChecked():
            cod_pagamento = self.codigoPagamentoLineEdit.text()
        if self.codigoPedidoCheckBox.isChecked():
            cod_pedido_teflon = self.codigoPedidoLineEdit.text()
        if self.codigoCondicaoPagamentoCheckBox.isChecked():
            cod_condicao_pagamento = self.codigoCondicaoPagamentoLineEdit.text()
        if self.pagoCheckBox.isChecked():
            pago = self.pagoComboBox.currentIndex()
        if self.conferidoCheckBox.isChecked():
            conferido = self.conferidoComboBox.currentIndex()
        if self.vencimentoCheckBox.isChecked():
            vencimento_data_inicial = self.vencimentoDataInicialDateEdit.date().toPython()
            vencimento_data_final = self.vencimentoDataFinalDateEdit.date().toPython()
        if self.dataPagoCheckBox.isChecked():
            data_pago_data_inicial = self.dataPagoInicialDateEdit.date().toPython()
            data_pago_data_final = self.dataPagoFinalDateEdit.date().toPython()
        if self.clienteCheckBox.isChecked():
            cliente = self.clienteLineEdit.text()

        model = PagamentoTableModel(
            cod_pagamento, cod_pedido_teflon, cod_condicao_pagamento,
            vencimento_data_inicial, vencimento_data_final,
            pago, data_pago_data_inicial, data_pago_data_final, conferido,
            cliente
        )

        self.model.setSourceModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    import sys
    from PySide.QtCore import Qt
    app = QApplication(sys.argv)
    a = PagamentoWidget()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())