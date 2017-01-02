
from PySide.QtCore import *
from PySide.QtGui import *
from sqlalchemy.orm import contains_eager

from bin.db.cliente import Cliente
from bin.db.vendedor import Vendedor
from bin.db.pedido_prima_linea import PedidoPrimaLinea
from bin.db.loja import Loja
from bin.db.session import Session


COD_PEDIDO = 0
COD_LOJA = 1
NOME_CLIENTE = 2
COD_ENDERECO = 3
NOME_VENDEDOR = 4
DATA_PEDIDO = 5
VALOR_TOTAL_DO_PEDIDO = 6
SITUACAO = 7


HEADERS = {COD_PEDIDO: "Pedido",
           COD_LOJA: "Loja",
           NOME_CLIENTE: "Cliente",
           COD_ENDERECO: "Endereço",
           NOME_VENDEDOR: "Vendedor",
           DATA_PEDIDO: "Data do Pedido",
           VALOR_TOTAL_DO_PEDIDO: "Valor Total",
           SITUACAO: "Situação"}


class PedidoPLTableModel(QAbstractTableModel):

    def __init__(self, initial_date=None, final_date=None, loja=None,
                 vendedor=None, cliente=None, pedido=None, endereco=None,
                 parent=None,):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(PedidoPrimaLinea) \
            .join(PedidoPrimaLinea.vendedor) \
            .join(PedidoPrimaLinea.cliente) \
            .join(PedidoPrimaLinea.loja) \
            .options(contains_eager("vendedor"),
                     contains_eager("cliente"),
                     contains_eager("loja"))

        if initial_date:
            query = query.filter(PedidoPrimaLinea.data_pedido >= initial_date)
        if final_date:
            query = query.filter(PedidoPrimaLinea.data_pedido <= final_date)
        if loja:
            if loja == "DF" or loja == "MG":
                query = query.filter(Loja.uf == loja)
            else:
                query = query.filter(PedidoPrimaLinea.cod_loja == loja)
        if vendedor:
            query = query.filter(Vendedor.nome_vendedor.ilike("%{}%".format(vendedor)))
        if cliente:
            query = query.filter(Cliente.nome.ilike("%{}%".format(cliente)))
        if pedido:
            query = query.filter(PedidoPrimaLinea.cod_pedido == pedido)
        if endereco:
            query = query.filter(PedidoPrimaLinea.cod_endereco == endereco)

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        pedido = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_PEDIDO:
                return pedido.cod_pedido
            elif index.column() == COD_LOJA:
                return pedido.cod_loja
            elif index.column() == NOME_CLIENTE:
                return pedido.cliente.nome
            elif index.column() == COD_ENDERECO:
                return pedido.cod_endereco
            elif index.column() == NOME_VENDEDOR:
                return pedido.vendedor.nome_vendedor
            elif index.column() == DATA_PEDIDO:
                return pedido.data_pedido.strftime("%d/%m/%y")
            elif index.column() == VALOR_TOTAL_DO_PEDIDO:
                return pedido.valor_total_pedido
            elif index.column() == SITUACAO:
                return pedido.get_formatted_situacao()

        elif role == Qt.BackgroundRole:
            if index.column() == SITUACAO:
                if pedido.situacao == "A":
                    return QColor("#D75F5F")
                elif pedido.situacao == "E":
                    return QColor("#46BC7B")

        elif role == Qt.AccessibleTextRole:
            if index.column() == DATA_PEDIDO:
                return pedido.data_pedido

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return HEADERS[section]
            else:
                return int(section) + 1

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication, QTableView
    app = QApplication(sys.argv)
    v = PedidoPLTableModel()
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())