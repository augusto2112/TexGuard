
from PySide.QtGui import *
from PySide.QtCore import Qt


class AbstractTableView(QTableView):
    def __init__(self, *args, **kwargs):
        QTableView.__init__(self, *args, **kwargs)
        self.subview = None
        self.menu = QMenu(self)
        self.y = None

    def contextMenuEvent(self, event):
        self.y = event.y()
        self.menu.popup(QCursor.pos())

    def set_current_subview(self, subview_class):
        if type(self.subview) is not subview_class and self.subview is not None:
            self.subview.close()
            self.subview = None
        if not self.subview:
            self.subview = subview_class()

    def abrir_endereco(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        cod_endereco = self.model().data(index, Qt.DisplayRole)

        self.subview.codEnderecoRadioButton.setChecked(True)
        self.subview.lineEdit.setText(str(cod_endereco))
        self.subview.set_model()
        self.subview.show()

    def abrir_endereco_nome(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        nome = self.model().data(index, Qt.DisplayRole)

        self.subview.nomeClienteRadioButton.setChecked(True)
        self.subview.lineEdit.setText(nome)
        self.subview.set_model()
        self.subview.show()

    def abrir_pedido(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        cod_pedido = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.pedidoLineEdit.setText(str(cod_pedido))
        self.subview.pedidoCheckBox.setChecked(True)
        self.subview.set_model()
        self.subview.show()

    def abrir_pedido_cliente(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        nome_cliente = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.clienteLineEdit.setText(nome_cliente)
        self.subview.clienteCheckBox.setChecked(True)
        self.subview.set_model()
        self.subview.show()

    def abrir_pedido_endereco(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        cod_endereco = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.enderecoLineEdit.setText(str(cod_endereco))
        self.subview.enderecoCheckBox.setChecked(True)
        self.subview.set_model()
        self.subview.show()

    def abrir_pedido_vendedor(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        vendedor = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.vendedorLineEdit.setText(vendedor)
        self.subview.vendedorCheckBox.setChecked(True)
        self.subview.set_model()
        self.subview.show()

    def abrir_cliente(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        nome_cliente = self.model().data(index, Qt.DisplayRole)

        self.subview.nomeRadioButton.setChecked(True)
        self.subview.lineEdit.setText(nome_cliente)
        self.subview.set_model()
        self.subview.show()

    def abrir_detalhes_pedido(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        pedido = self.model().data(index, Qt.DisplayRole)

        self.subview.pedidoLineEdit.setText(pedido)
        self.subview.pesquisar_pedido()
        self.subview.show()

    def abrir_comissao(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        pedido = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.pedidoCheckBox.setChecked(True)
        self.subview.pedidoLineEdit.setText(str(pedido))
        self.subview.set_model()
        self.subview.show()

    def abrir_pagamento(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        pedido = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.codigoPedidoCheckBox.setChecked(True)
        self.subview.codigoPedidoLineEdit.setText(str(pedido))
        self.subview.set_model()
        self.subview.show()

    def abrir_produto(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        cod_produto = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.codProdutoCheckBox.setChecked(True)
        self.subview.codProdutoLineEdit.setText(str(cod_produto))
        self.subview.set_model()
        self.subview.show()

    def abrir_aplicacao(self, column):
        index = self.model().index(self.rowAt(self.y), column)
        cod_produto = self.model().data(index, Qt.DisplayRole)

        self.subview.set_checkboxes_unchecked()
        self.subview.codProdutoCheckBox.setChecked(True)
        self.subview.codProdutoLineEdit.setText(str(cod_produto))
        self.subview.set_model()
        self.subview.show()