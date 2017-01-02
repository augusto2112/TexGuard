
from PySide.QtCore import *

from bin.db.cliente import Cliente
from bin.db.session import Session

CODIGO_CLIENTE = 0
NOME_CLIENTE = 1
CPF = 2


HEADERS = {CODIGO_CLIENTE: "Código",
           NOME_CLIENTE: "Nome",
           CPF: "CPF"}


class ClienteTableModel(QAbstractTableModel):
    def __init__(self, nome=None, codigo=None, parent=None):
        QAbstractTableModel.__init__(self, parent)
        session = Session()
        query = session.query(Cliente)
        if nome:
            query = query.filter(Cliente.nome.ilike("%{}%".format(nome)))
        if codigo:
            query = query.filter(Cliente.cod_cliente.ilike("%{}%".format(codigo)))

        self._data = query.all()
        session.close()

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(HEADERS)

    def data(self, index, role):
        cliente = self._data[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == CODIGO_CLIENTE:
                return cliente.cod_cliente
            elif index.column() == NOME_CLIENTE:
                return cliente.nome
            elif index.column() == CPF:
                return cliente.cpf

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
    v = ClienteTableModel()
    view = QTableView()
    view.setModel(v)
    view.resize(1200, 1000)
    view.show()
    sys.exit(app.exec_())