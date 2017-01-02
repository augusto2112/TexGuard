
from decimal import Decimal
from monthdelta import monthdelta

from PySide.QtGui import *


from bin.db.session import Session
from bin.db.condicao_pagamento import CondicaoPagamento
from bin.db.pagamento import Pagamento

from bin.ui.cadastro_pagamento_ui import Ui_CadastroPagamentoDialog


class CadastroPagamentoDialog(Ui_CadastroPagamentoDialog, QDialog):
    def __init__(self, pedido_teflon, parent=None):
        QDialog.__init__(self, parent)
        self.ui = self.setupUi(self)

        condicoes_session = Session()
        self.condicoes_pagamento = condicoes_session.query(CondicaoPagamento).all()
        condicoes_session.close()

        self.comboBox.addItems([condicao_pagamento.descricao for condicao_pagamento in self.condicoes_pagamento])
        self.comboBox.currentIndexChanged.connect(self.load_fields)

        self.primeiroLineEdit.setValidator(QDoubleValidator(0, 9999999, 2, self))
        self.segundoLineEdit.setValidator(QDoubleValidator(0, 9999999, 2, self))
        self.terceiroLineEdit.setValidator(QDoubleValidator(0, 9999999, 2, self))

        self.primeiroDateEdit.setDate(pedido_teflon.data_pedido)
        self.segundoDateEdit.setDate(pedido_teflon.data_pedido + monthdelta(1))
        self.terceiroDateEdit.setDate(pedido_teflon.data_pedido + monthdelta(2))

        self.primeiroDateEdit.dateChanged.connect(self.change_dates)

        self.pedido_teflon = pedido_teflon
        self.load_fields(0)

    def change_dates(self):
        date = self.primeiroDateEdit.date().toPython()
        self.segundoDateEdit.setDate(date + monthdelta(1))
        self.terceiroDateEdit.setDate(date + monthdelta(2))


    def load_fields(self, index):
        self.reset_fields()
        self.condicao_pagamento = self.condicoes_pagamento[index]
        if self.condicao_pagamento.parcelas < 2:
            self.segundoLineEdit.hide()
            self.segundoLabel.hide()
            self.segundoDateEdit.hide()
        if self.condicao_pagamento.parcelas < 3:
            self.terceiroLineEdit.hide()
            self.terceiroLabel.hide()
            self.terceiroDateEdit.hide()

        if self.comboBox.currentIndex() == 9: # 30 dias
            self.primeiroDateEdit.setDate(self.primeiroDateEdit.date().toPython() + monthdelta(1))

        self.set_fields(self.condicao_pagamento.parcelas)

    def set_fields(self, parcelas):
        if self.pedido_teflon.valor:
            self.primeiroLineEdit.setText(str(round(Decimal(self.pedido_teflon.valor / parcelas), 2)))
            if parcelas == 2 or parcelas == 3:
                self.segundoLineEdit.setText(str(round(Decimal(self.pedido_teflon.valor / parcelas), 2)))
            if parcelas == 3:
                self.terceiroLineEdit.setText(str(round(Decimal(self.pedido_teflon.valor / parcelas), 2)))

    def reset_fields(self):
        self.primeiroLineEdit.setText("")
        self.segundoLineEdit.setText("")
        self.terceiroLineEdit.setText("")

        self.segundoLineEdit.show()
        self.segundoLabel.show()
        self.segundoDateEdit.show()
        self.terceiroLineEdit.show()
        self.terceiroLabel.show()
        self.terceiroDateEdit.show()

    def accept(self):
        if self.primeiroLineEdit.text() == "" \
                and self.segundoLineEdit.text() == "" \
                and self.terceiroLineEdit.text() == "":
            QMessageBox.warning(self, "Preencha os campos requeridos",
                                'Preencha os valores')
        else:
            for lineEdit, dateEdit in zip((self.primeiroLineEdit, self.segundoLineEdit, self.terceiroLineEdit),
                                          (self.primeiroDateEdit, self.segundoDateEdit, self.terceiroDateEdit)):
                if lineEdit.text() != "" and lineEdit.isHidden() is False:
                    valor = float(lineEdit.text())
                    pagamento = Pagamento(pedido_teflon=self.pedido_teflon,
                                                           condicao_pagamento=self.condicao_pagamento,
                                                           valor=valor,
                                                           vencimento=dateEdit.date().toPython())
            QDialog.accept(self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = CadastroPagamentoDialog(Session(), )
    dialog.show()
    sys.exit(app.exec_())
