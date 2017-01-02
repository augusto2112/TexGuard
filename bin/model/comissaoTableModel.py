
from PySide.QtCore import *
from sqlalchemy import or_
from sqlalchemy.orm import joinedload, contains_eager

from bin.db.comissao import Comissao
from bin.db.vendedor import Vendedor

from bin.db.session import Session

VENDEDOR = 0
PEDIDO = 1
LOJA = 2
COMISSAO = 3
PERCENTUAL = 4
TOTAL = 5
NA_LOJA = 6
PAGO = 7

HEADERS = {VENDEDOR: "Vendedor",
           PEDIDO: "Pedido",
           LOJA: "Loja",
           COMISSAO: "Comissão",
           PERCENTUAL: "Percentual",
           TOTAL: "Total",
           NA_LOJA: "Na Loja",
           PAGO: "Pago"}


class ComissaoTableModel(QAbstractTableModel):

    def __init__(self, vendedor=None, pedido=None,
                 initial_date=None, final_date=None, loja=None, parent=None):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(Comissao) \
                .join(Comissao.vendedor)\
                .options(contains_eager(Comissao.vendedor),
                         joinedload('pedido_teflon')) \
                .filter(Comissao.status_pagamento != 2)

        if vendedor:
            query = query.filter(Vendedor.nome_vendedor.ilike("%{}%".format(vendedor)))
        if pedido:
            query = query.filter(Comissao.cod_pedido_teflon == pedido)
        if initial_date and final_date:
            query = query.filter(Comissao.data_pagamento.between(initial_date, final_date))
        if loja:
            query = query.filter(Vendedor.cod_loja == loja)

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        elif index.column() == PAGO or index.column() == NA_LOJA:
            return Qt.ItemFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        else:
            return QAbstractTableModel.flags(self, index)

    def data(self, index, role):
        comissao = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == VENDEDOR:
                return comissao.vendedor.nome_vendedor
            elif index.column() == PEDIDO:
                return comissao.cod_pedido_teflon
            elif index.column() == LOJA:
                return comissao.vendedor.cod_loja
            elif index.column() == PERCENTUAL:
                return comissao.vendedor.percentual_comissao
            elif index.column() == TOTAL:
                return comissao.pedido_teflon.valor  # ALTERAR PARA valor_total_tefloN
            elif index.column() == COMISSAO:
                return comissao.valor

        if role == Qt.CheckStateRole:
            if index.column() == PAGO:
                return comissao.status_pagamento == 2
            elif index.column() == NA_LOJA:
                return comissao.status_pagamento == 1

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self._data):
            comissao = self._data[index.row()]
            if index.column() == NA_LOJA:
                if comissao.status_pagamento != 1:
                    comissao.status_pagamento = 1
                else:
                    comissao.status_pagamento = 0
            elif index.column() == PAGO:
                if comissao.status_pagamento != 2:
                    comissao.status_pagamento = 2
                else:
                    comissao.status_pagamento = 0

            self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                      index.sibling(index.row(), NA_LOJA), index.sibling(index.row(), PAGO))
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return HEADERS[section]
            else:
                return int(section) + 1

    def commit(self):
        session = Session()
        session.add_all(self._data)
        session.commit()
        session.close()

if __name__ == '__main__':
    import sys
    from datetime import date
    from PySide.QtGui import QApplication, QTableView
    app = QApplication(sys.argv)
    v = ComissaoTableModel(initial_date=date(2014, 1, 1), final_date=date(2014, 12, 30))
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())