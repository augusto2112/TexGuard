
from PySide.QtCore import *

from bin.db.produto import Produto
from bin.db.session import Session


COD_PEDIDO = 0
NUM_ITEM = 1
COD_PRODUTO = 2
COD_COMPLEMENTO = 3
COD_ACABAMENTO = 4
DESC_PRODUTO = 5
MOSTRUARIO = 6
QUANTIDADE_PRODUTO = 7
PRECO_UNITARIO_CHEIO = 8
PRECO_PROPORCIONAL = 9
DATA_ENTREGA1 = 10
DATA_ENTREGA2 = 11
SITUACAO = 12
TEM_TEFLON = 13

HEADERS = {COD_PEDIDO: "Pedido",
           NUM_ITEM: "Número do item",
           COD_PRODUTO: "Código Produto",
           COD_COMPLEMENTO: "Código Complemento",
           COD_ACABAMENTO: "Código Acabamento",
           DESC_PRODUTO: "Descrição Produto",
           MOSTRUARIO: "Mostruário",
           QUANTIDADE_PRODUTO: "Quantidade Produto",
           PRECO_UNITARIO_CHEIO: "Preço Unitário Cheio",
           PRECO_PROPORCIONAL: "Preço Proporcional",
           DATA_ENTREGA1: "Data Entrega",
           DATA_ENTREGA2: "Data Entrega 2",
           SITUACAO: "Situação",
           TEM_TEFLON: "Tem Teflon"}


class ProdutoTableModel(QAbstractTableModel):

    def __init__(self, pedido=None, cod_produto=None, vendeu_teflon=None, parent=None):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(Produto)

        if pedido:
            query = query.filter(Produto.cod_pedido == pedido)
        if cod_produto:
            query = query.filter(Produto.cod_produto == cod_produto)
        if vendeu_teflon:
            query = query.filter(Produto.vendeu_teflon == vendeu_teflon)

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        produto = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_PEDIDO:
                return produto.cod_pedido
            elif index.column() == NUM_ITEM:
                return produto.num_item
            elif index.column() == COD_PRODUTO:
                return produto.cod_produto
            elif index.column() == COD_COMPLEMENTO:
                return produto.cod_complemento
            elif index.column() == COD_ACABAMENTO:
                return produto.cod_acabamento
            elif index.column() == DESC_PRODUTO:
                return produto.desc_produto
            elif index.column() == MOSTRUARIO:
                return produto.mostruario
            elif index.column() == QUANTIDADE_PRODUTO:
                return produto.quantidade_pedido
            elif index.column() == PRECO_UNITARIO_CHEIO:
                return produto.preco_unitario_cheio
            elif index.column() == PRECO_PROPORCIONAL:
                return produto.preco_proporcional
            elif index.column() == DATA_ENTREGA1:
                return produto.data_entrega_primaria.strftime("%d/%m/%y")
            elif index.column() == DATA_ENTREGA2:
                return produto.data_entrega_secundaria.strftime("%d/%m/%y")
            elif index.column() == SITUACAO:
                return produto.get_formatted_situacao()
            elif index.column() == TEM_TEFLON:
                return produto.get_formatted_vendeu_teflon()

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
    model = ProdutoTableModel('09101302')
    view = QTableView()
    view.setModel(model)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())