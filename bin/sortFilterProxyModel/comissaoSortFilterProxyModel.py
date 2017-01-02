
from PySide.QtCore import *
from PySide.QtGui import *

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


class ComissaoSortFilterProxyModel(QSortFilterProxyModel):
    def lessThan(self, left, right):
        if left.column() == NA_LOJA or left.column() == PAGO:
            if left.column() == NA_LOJA:
                left_sibling = left.sibling(left.row(), left.column() + 1)
                right_sibling = right.sibling(right.row(), right.column() + 1)
            else:
                left_sibling = left.sibling(left.row(), left.column() - 1)
                right_sibling = right.sibling(right.row(), right.column() - 1)
                left, left_sibling, right, right_sibling = left_sibling, left, right_sibling, right

            left_data = self.sourceModel().data(left, role=Qt.CheckStateRole)
            right_data = self.sourceModel().data(right, role=Qt.CheckStateRole)

            left_sibling_data = self.sourceModel().data(left_sibling, role=Qt.CheckStateRole)
            right_sibling_data = self.sourceModel().data(right_sibling, role=Qt.CheckStateRole)

            if left_sibling_data and not right_sibling_data:
                return False
            elif right_sibling_data and not left_sibling_data:
                return True
            elif left_data and not right_data:
                return False
            elif right_data and not left_data:
                return True
            else:
                return True
        else:
            return QSortFilterProxyModel.lessThan(self, left, right)