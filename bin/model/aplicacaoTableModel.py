
from PySide.QtCore import *

from sqlalchemy.orm import contains_eager

from bin.db.aplicacao import Aplicacao
from bin.db.pedido_teflon import PedidoTeflon

from bin.db.session import Session

COD_APLICACAO = 0
COD_PEDIDO_TEFLON = 1
COD_PEDIDO_PL = 2
COD_PRODUTO = 3
QUANTIDADE_PRODUTO = 4

HEADERS = {COD_APLICACAO: "Código Aplicação",
           COD_PEDIDO_TEFLON: "Código Pedido Teflon",
           COD_PEDIDO_PL: "Código Pedido PL",
           COD_PRODUTO: "Código Produto",
           QUANTIDADE_PRODUTO: "Quantidade de Produtos"}


class AplicacaoTableModel(QAbstractTableModel):
    def __init__(self, pedido_teflon=None, pedido_pl=None, cod_produto=None,
                 parent=None):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(Aplicacao) \
            .join(Aplicacao.pedido_teflon) \
            .options(contains_eager('pedido_teflon'))

        if pedido_teflon:
            query = query.filter(Aplicacao.cod_pedido_teflon == pedido_teflon)
        if pedido_pl:
            query = query.filter(PedidoTeflon.cod_pedido_pl == pedido_pl)
        if cod_produto:
            query = query.filter(Aplicacao.cod_produto == cod_produto)

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        aplicacao = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_APLICACAO:
                return aplicacao.cod_aplicacao
            elif index.column() == COD_PEDIDO_TEFLON:
                return aplicacao.cod_pedido_teflon
            elif index.column() == COD_PEDIDO_PL:
                return aplicacao.pedido_teflon.cod_pedido_pl
            elif index.column() == COD_PRODUTO:
                return aplicacao.cod_produto
            elif index.column() == QUANTIDADE_PRODUTO:
                return aplicacao.quantidade_produto

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return HEADERS[section]
            else:
                return int(section) + 1


if __name__ == '__main__':
    import sys
    # from PyQt5.QtGui import QApplication
    from PySide.QtGui import QApplication, QTableView
    app = QApplication(sys.argv)
    v = AplicacaoTableModel()
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())