
from PySide.QtGui import *

from bin.db.cliente import Cliente
from bin.db.endereco import Endereco
from bin.db.session import Session

from bin.ui.cadastro_cliente_ui import Ui_CadastroClienteDialog


class CadastroClienteDialog(Ui_CadastroClienteDialog, QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = self.setupUi(self)

    def accept(self):
        required_fields = (self.nomeLineEdit, self.cpfLineEdit,
                           self.enderecoLineEdit, self.bairroLineEdit, self.cepLineEdit,
                           self.cidadeLineEdit, self.ufLineEdit)
        for field in required_fields:
            if field.text() == "":
                QMessageBox.warning(self, "Preencha os campos requeridos",
                                    'Os campos "Nome", "CPF", "Endereço", "Bairro", "CEP",'
                                    '"Cidade" e "UF" são obrigatórios')
                break
        else:
            self.cliente = Cliente(nome=self.nomeLineEdit.text(),
                                             cpf=self.cpfLineEdit.text())

            self.endereco = Endereco(cliente=self.cliente, cep=self.cepLineEdit.text(),
                                                endereco=self.enderecoLineEdit.text(),
                                                bairro=self.bairroLineEdit.text(),
                                                cidade=self.cidadeLineEdit.text(),
                                                uf=self.ufLineEdit.text(),
                                                fone=self.telefoneResidencialLineEdit.text(),
                                                fone2=self.celularLineEdit.text(),
                                                email=self.emailLineEdit.text(),
                                                ponto_referencia_cliente=self.pontoDeReferenciaLineEdit.text())
            session = Session()
            session.add(self.endereco)
            session.expunge_all()
            session.commit()
            session.close()
            QDialog.accept(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = CadastroClienteDialog()
    dialog.show()
    sys.exit(app.exec_())

