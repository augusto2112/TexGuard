
from PySide.QtCore import *

from bin.db.produto import Produto
from bin.db.aplicacao import Aplicacao
from bin.db.session import Session


COD_PRODUTO = 0
COD_COMPLEMENTO = 1
COD_ACABAMENTO = 2
DESC_PRODUTO = 3
QUANTIDADE_PEDIDO = 4
QUANTIDADE_APLICADA = 5
QUANTIDADE_TEFLON = 6

HEADERS = {COD_PRODUTO: "Código Produto",
           COD_COMPLEMENTO: "Código Complemento",
           COD_ACABAMENTO: "Código Acabamento",
           DESC_PRODUTO: "Descrição Produto",
           QUANTIDADE_PEDIDO: "Quantidade Pedido",
           QUANTIDADE_APLICADA: "Quantidade Aplicada",
           QUANTIDADE_TEFLON: "Quantidade Teflon"}


class SelecaoProdutoTableModel(QAbstractTableModel):

    def __init__(self, pedido_teflon, parent=None):
        # self._aplicacoes sao as aplicacoes ja existentes
        # self._novas_aplicacoes sao as aplicacoes que serao cadastradas, comecam como lista de 0s
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        print(pedido_teflon.cod_pedido_pl)
        query = session.query(Produto)\
            .filter(Produto.cod_pedido == pedido_teflon.cod_pedido_pl)

        self._data = query.all()
        self._aplicacoes = []

        for produto in self._data:
            if produto.aplicacoes:
                self._aplicacoes.append(sum([aplicacao.quantidade_produto for aplicacao in produto.aplicacoes]))
            else:
                self._aplicacoes.append(0)

        self._novas_aplicacoes = [0 for _ in self._data]

        self.pedido_teflon = pedido_teflon
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        produto = self._data[index.row()]
        aplicacao = self._novas_aplicacoes[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_PRODUTO:
                return produto.cod_produto
            elif index.column() == COD_COMPLEMENTO:
                return produto.cod_complemento
            elif index.column() == COD_ACABAMENTO:
                return produto.cod_acabamento
            elif index.column() == DESC_PRODUTO:
                return produto.desc_produto
            elif index.column() == QUANTIDADE_PEDIDO:
                return produto.quantidade_pedido
            elif index.column() ==  QUANTIDADE_APLICADA:
                return self._aplicacoes[index.row()]
            elif index.column() == QUANTIDADE_TEFLON:
                if aplicacao == 0:
                    return aplicacao
                else:
                    return aplicacao.quantidade_produto

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return HEADERS[section]
            else:
                return int(section) + 1

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        elif index.column() == QUANTIDADE_TEFLON:
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)
        else:
            return QAbstractTableModel.flags(self, index)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self._data):
            aplicacao = self._novas_aplicacoes[index.row()]
            if index.column() == QUANTIDADE_TEFLON:
                try:
                    quantidade = int(value)
                except ValueError:
                    return False
                produto = self._data[index.row()]
                total_aplicacoes = quantidade + self._aplicacoes[index.row()] # maximo de aplicaco + aplicacoes ja existentes
                if quantidade == 0:
                    self._novas_aplicacoes[index.row()] = 0
                    self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
                elif total_aplicacoes <= produto.quantidade_pedido and quantidade > 0:
                    if aplicacao == 0:
                        aplicacao = Aplicacao(produto=produto, pedido_teflon=self.pedido_teflon)
                    aplicacao.quantidade_produto = quantidade
                    self._novas_aplicacoes[index.row()] = aplicacao
                    self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
                return True

        return False

    def get_quantidade_novas_aplicacoes(self):
        aplicacoes = []
        for aplicacao in self._novas_aplicacoes:
            if aplicacao != 0:
                aplicacoes.append(aplicacao)
        return len(aplicacoes)

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication, QTableView
    from bin.db.pedido_teflon import PedidoTeflon
    app = QApplication(sys.argv)
    session = Session()
    pedido_teflon = session.query(PedidoTeflon).filter(PedidoTeflon.cod_pedido == 500).one()
    model = SelecaoProdutoTableModel(pedido_teflon)
    view = QTableView()
    view.setModel(model)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())