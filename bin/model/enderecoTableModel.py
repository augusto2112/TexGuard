
from PySide.QtCore import *

from sqlalchemy.orm import contains_eager

from bin.db.cliente import Cliente
from bin.db.endereco import Endereco
from bin.db.session import Session


COD_ENDERECO = 0
NOME_CLIENTE = 1
ENDERECO = 2
BAIRRO = 3
CEP = 4
CIDADE = 5
UF = 6
FONE = 7
FONE2 = 8
PONTO_REFERENCIA = 9


HEADERS = {COD_ENDERECO: "Código de Endereço",
           NOME_CLIENTE: "Nome",
           CEP: "CEP",
           ENDERECO: "Endereço",
           BAIRRO: "Bairro",
           CIDADE: "Cidade",
           UF: "UF",
           FONE: "Telefone",
           FONE2: "Telefone 2",
           PONTO_REFERENCIA: "Ponto de Referência"}


class EnderecoTableModel(QAbstractTableModel):
    def __init__(self, nome_cliente=None, cod_cliente=None, cep=None,
                 endereco=None, cidade=None, uf=None, cod_endereco=None, parent=None):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(Endereco) \
            .join(Endereco.cliente) \
            .options(contains_eager('cliente'))

        if nome_cliente:
            query = query.filter(Cliente.nome.ilike("%{}%".format(nome_cliente)))
        if cod_cliente:
            query = query.filter(Cliente.cod_cliente == cod_cliente)
        if cep:
            query = query.filter(Endereco.cep.ilike("%{}%".format(cep)))
        if endereco:
            query = query.filter(Endereco.endereco.ilike("%{}%".format(endereco)))
        if cidade:
            query = query.filter(Endereco.cidade.ilike("%{}%".format(cidade)))
        if uf:
            query = query.filter(Endereco.uf.ilike("%{}%".format(uf)))
        if cod_endereco:
            query = query.filter(Endereco.cod_endereco == cod_endereco)

        self._data = query.all()
        session.close()

    # def __init__(self, data, parent=None):
    #     QAbstractTableModel.__init__(self, parent)
    #     self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        endereco = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == COD_ENDERECO:
                return endereco.cod_endereco
            elif index.column() == NOME_CLIENTE:
                return endereco.cliente.nome
            elif index.column() == ENDERECO:
                return endereco.endereco
            elif index.column() == BAIRRO:
                return endereco.bairro
            elif index.column() == CEP:
                return endereco.cep
            elif index.column() == CIDADE:
                return endereco.cidade
            elif index.column() == UF:
                return endereco.uf
            elif index.column() == FONE:
                return endereco.fone
            elif index.column() == FONE2:
                return endereco.fone2
            elif index.column() == PONTO_REFERENCIA:
                return endereco.ponto_referencia_cliente

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
    v = EnderecoTableModel()
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())