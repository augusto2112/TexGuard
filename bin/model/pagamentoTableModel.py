
from PySide.QtCore import *

from sqlalchemy.orm import contains_eager

from bin.db.pagamento import Pagamento
from bin.db.condicao_pagamento import CondicaoPagamento
from bin.db.pedido_teflon import PedidoTeflon
from bin.db.cliente import Cliente

from bin.db.session import Session


COD_PAGAMENTO = 0
COD_PEDIDO_TEFLON = 1
CLIENTE = 2
COD_CONDICAO_PAGAMENTO = 3
DESCRICAO_CONDICAO_PAGAMENTO = 4
VALOR = 5
VENCIMENTO = 6
PAGO = 7
DATA_PAGO = 8
CONFERIDO = 9


HEADERS = {COD_PAGAMENTO: "Código Pagmento",
           COD_PEDIDO_TEFLON: "Código Pedido Teflon",
           CLIENTE: "Cliente",
           COD_CONDICAO_PAGAMENTO: "Código Condição de Pagamento",
           DESCRICAO_CONDICAO_PAGAMENTO: "Descrição Condição de Pagamento",
           VALOR: "Valor",
           VENCIMENTO: "Vencimento",
           PAGO: "Pago",
           DATA_PAGO: "Data Pago",
           CONFERIDO: "Conferido"}


class PagamentoTableModel(QAbstractTableModel):
    def __init__(self, cod_pagamento=None, cod_pedido_teflon=None,
                 cod_condicao_pagamento=None, vencimento_inicial=None,
                 vencimento_final=None, pago=None, data_pago_inicial=None,
                 data_pago_final=None, conferido=None, cliente=None,
                 parent=None):
        QAbstractTableModel.__init__(self, parent)

        session = Session()
        query = session.query(Pagamento) \
            .join(Pagamento.condicao_pagamento) \
            .join(Pagamento.pedido_teflon) \
            .join(PedidoTeflon.cliente) \
            .options(contains_eager('condicao_pagamento'),
                     contains_eager('pedido_teflon'),
                     contains_eager('pedido_teflon.cliente'))

        if cod_pagamento:
            query = query.filter(Pagamento.cod_pagamento == cod_pagamento)
        if cod_pedido_teflon:
            query = query.filter(Pagamento.cod_pedido_teflon == cod_pedido_teflon)
        if cod_condicao_pagamento:
            query = query.filter(Pagamento.cod_condicao_pagamento == cod_condicao_pagamento)
        if vencimento_inicial and vencimento_final:
            query = query.filter(Pagamento.vencimento.between(vencimento_inicial, vencimento_final))
        if pago:
            query = query.filter(Pagamento.pago == pago)
        if data_pago_inicial and data_pago_final:
            query = query.filter(Pagamento.data_pago.between(data_pago_inicial, data_pago_final))
        if conferido:
            query = query.filter(Pagamento.conferido == conferido)
        if cliente:
            query = query.filter(Cliente.nome.ilike("%{}%".format(cliente)))

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        pagamento = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_PAGAMENTO:
                return pagamento.cod_pagamento
            elif index.column() == COD_PEDIDO_TEFLON:
                return pagamento.cod_pedido_teflon
            elif index.column() == CLIENTE:
                return pagamento.pedido_teflon.cliente.nome
            elif index.column() == COD_CONDICAO_PAGAMENTO:
                return pagamento.cod_condicao_pagamento
            elif index.column() == DESCRICAO_CONDICAO_PAGAMENTO:
                return pagamento.condicao_pagamento.descricao
            elif index.column() == VALOR:
                return pagamento.valor
            elif index.column() == VENCIMENTO:
                return pagamento.vencimento.strftime("%d/%m/%y")
            elif index.column() == PAGO:
                return pagamento.get_formatted_pago()
            elif index.column() == DATA_PAGO:
                return pagamento.get_formatted_data_pago()
            elif index.column() == CONFERIDO:
                return pagamento.get_formatted_conferido()

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
    v = PagamentoTableModel()
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())