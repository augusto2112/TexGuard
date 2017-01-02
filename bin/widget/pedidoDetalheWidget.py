from PySide.QtGui import *
from PySide.QtCore import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import contains_eager

from bin.db.session import Session

from bin.db.pedido_prima_linea import PedidoPrimaLinea
from bin.model.produtoTableModel import ProdutoTableModel
from bin.ui.pedido_detalhe_widget_ui import Ui_PedidoDetalhe


class PedidoDetalhe(Ui_PedidoDetalhe, QWidget):
    def __init__(self, pedido=None, parent=None):
        QWidget.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.pesquisarPushButton.clicked.connect(self.pesquisar_pedido)

        self._produtoModel = QSortFilterProxyModel()
        self.produtoTableView.setModel(self._produtoModel)
        self.produtoTableView.setSortingEnabled(True)

        validator = QIntValidator(0, 999999999)
        self.pedidoLineEdit.setValidator(validator)

        if pedido:
            self.pedidoLineEdit.setText(pedido)
            self.pesquisar_pedido()

    def pesquisar_pedido(self):
        session = Session()
        try:
            pedido = session.query(PedidoPrimaLinea).\
                join(PedidoPrimaLinea.vendedor).\
                join(PedidoPrimaLinea.cliente).\
                join(PedidoPrimaLinea.endereco).\
                options(contains_eager("vendedor"),
                        contains_eager("cliente"),
                        contains_eager("endereco")).\
                filter(PedidoPrimaLinea.cod_pedido == self.pedidoLineEdit.text()).one()

            self.codigoLineEdit.setText(pedido.cod_pedido)
            self.lojaLineEdit.setText(pedido.cod_loja)
            self.clienteLineEdit.setText(pedido.cliente.nome)
            self.vendedorLineEdit.setText(pedido.vendedor.nome_vendedor)
            self.valorLineEdit.setText(str(pedido.valor_total_pedido))
            self.dataPedidoDateEdit.setDate(pedido.data_pedido)
            self.enderecoLineEdit.setText(pedido.endereco.endereco)
            self.cepLineEdit.setText(pedido.endereco.cep)
            self.bairroLineEdit.setText(pedido.endereco.bairro)
            self.cidadeLineEdit.setText(pedido.endereco.cidade)
            self.referenciaLineEdit.setText(pedido.endereco.ponto_referencia_cliente)
            self.foneLineEdit.setText(pedido.endereco.fone)
            self.fone2LineEdit.setText(pedido.endereco.fone2)

            self._produtoModel.setSourceModel(ProdutoTableModel(pedido.cod_pedido))
            self.produtoTableView.resizeColumnsToContents()

        except NoResultFound:
            pass
        except MultipleResultsFound:
            QMessageBox.warning(self, "Erro", "O banco de dados retornou mais de um pedido, issso não deveria "
                                "ser possível. Favor contactar o programador com o número do pedido")
        finally:
            session.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = PedidoDetalhe()
    a.setFocusPolicy(Qt.StrongFocus)
    a.activateWindow()
    a.showMaximized()
    sys.exit(app.exec_())