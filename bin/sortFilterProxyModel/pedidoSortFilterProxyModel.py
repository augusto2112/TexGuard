from PySide.QtCore import *
from PySide.QtGui import *


class PedidoSortFilterProxyModel(QSortFilterProxyModel):
    def lessThan(self, left, right):
        source_model = self.sourceModel()
        if source_model.headerData(left.column(), Qt.Horizontal) == "Data do Pedido":
            left_data = source_model.data(left, Qt.AccessibleTextRole)
            right_data = source_model.data(right, Qt.AccessibleTextRole)
            return left_data < right_data
        else:
            return QSortFilterProxyModel.lessThan(self, left, right)
