
from PySide.QtCore import *
from sqlalchemy.orm import contains_eager, joinedload

from bin.db.cliente import Cliente
from bin.db.vendedor import Vendedor
from bin.db.pedido_teflon import PedidoTeflon
from bin.db.session import Session

COD_PEDIDO = 0
COD_LOJA = 1
COD_PEDIDO_PL = 2
NOME_CLIENTE = 3
COD_ENDERECO = 4
NOME_VENDEDOR = 5
DATA_PEDIDO = 6
DATA_CADASTRO = 7
VALOR = 8
TIPO_VENDA = 9


HEADERS = {COD_PEDIDO: "Pedido",
           COD_LOJA: "Loja",
           COD_PEDIDO_PL: "Pedido Prima Linea",
           NOME_CLIENTE: "Cliente",
           COD_ENDERECO: "Endereço",
           NOME_VENDEDOR: "Vendedor",
           DATA_PEDIDO: "Data do Pedido",
           DATA_CADASTRO: "Data do Cadastro",
           VALOR: "Valor",
           TIPO_VENDA: "Tipo de Venda"}


class PedidoTeflonTableModel(QAbstractTableModel):

    def __init__(self, initial_date=None, final_date=None, loja=None,
                 vendedor=None, cliente=None, pedido=None, endereco=None,
                 parent=None,):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(PedidoTeflon) \
            .join(PedidoTeflon.vendedor) \
            .join(PedidoTeflon.cliente) \
            .options(contains_eager("vendedor"),
                     contains_eager('cliente'))

        if initial_date:
            query = query.filter(PedidoTeflon.data_pedido >= initial_date)
        if final_date:
            query = query.filter(PedidoTeflon.data_pedido <= final_date)
        if loja:
            query = query.filter(PedidoTeflon.cod_loja == loja)
        if vendedor:
            query = query.filter(Vendedor.nome_vendedor.ilike("%{}%".format(vendedor)))
        if cliente:
            query = query.filter(Cliente.nome.ilike("%{}%".format(cliente)))
        if pedido:
            query = query.filter(PedidoTeflon.cod_pedido == pedido)
        if endereco:
            query = query.filter(PedidoTeflon.cod_endereco == endereco)

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
            elif index.column() == COD_PEDIDO_PL:
                return pedido.get_formatted_cod_pedido_pl()
            elif index.column() == NOME_CLIENTE:
                return pedido.cliente.nome
            elif index.column() == COD_ENDERECO:
                return pedido.cod_endereco
            elif index.column() == NOME_VENDEDOR:
                return pedido.vendedor.nome_vendedor
            elif index.column() == DATA_PEDIDO:
                return pedido.data_pedido.strftime("%d/%m/%y")
            elif index.column() ==  DATA_CADASTRO:
                try:
                    return pedido.data_cadastro.strftime("%d/%m/%y")
                except AttributeError:
                    return "Sem data"
            elif index.column() == VALOR:
                return pedido.valor
            elif index.column() == TIPO_VENDA:
                return pedido.get_formatted_tipo_venda()

        elif role == Qt.AccessibleTextRole:
            if index.column() == DATA_PEDIDO:
                return pedido.data_pedido

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return HEADERS[section]
            else:
                return int(section) + 1

    def excluir_pedido(self, cod_pedido):
        session = Session()
        pedido = session.query(PedidoTeflon)\
            .options(joinedload('pagamentos'),
                     joinedload('comissoes'),
                     joinedload('aplicacoes'))\
            .filter(PedidoTeflon.cod_pedido ==  cod_pedido).one()
        for row in pedido.pagamentos + pedido.comissoes + pedido.aplicacoes:
            session.delete(row)
        session.delete(pedido)
        session.commit()
        session.close()

        for pedido in self._data:
            if pedido.cod_pedido == cod_pedido:
                self._data.remove(pedido)
                break
        self.modelReset.emit()

if __name__ == '__main__':
    import sys
    from datetime import date
    from PySide.QtGui import QApplication, QTableView
    app = QApplication(sys.argv)
    v = PedidoTeflonTableModel(initial_date=date(2014, 1, 1), final_date=date(2014, 12, 30))
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())