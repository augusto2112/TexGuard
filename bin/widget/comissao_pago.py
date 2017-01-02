from datetime import date

from PySide.QtGui import *

from bin.ui.comissao_pago_dialog_ui import Ui_Dialog

from bin.scripts.atualizarComissoes import marcar_comissoes_pago


class ComissaoPagoDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = self.setupUi(self)
        self.dateEdit.setDate(date.today())

    def accept(self, *args, **kwargs):
        confirmacao = QMessageBox.question(self, "Confirmação", "Tem certeza que deseja marcar as comissões como pagas?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if confirmacao == QMessageBox.Yes:
            marcar_comissoes_pago(self.dateEdit.date().toPython(), self.vendedoresRadioButton.isChecked())
            QMessageBox.information(self, "Sucesso", "Comissões marcardas com sucesso!")
            QDialog.accept(self, *args, **kwargs)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = ComissaoPagoDialog()
    dialog.show()
    sys.exit(app.exec_())
