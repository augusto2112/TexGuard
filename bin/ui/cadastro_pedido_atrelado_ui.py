# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_pedido_atrelado.ui'
#
# Created: Thu May  5 16:18:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CadastroPedidoAtreladoDialog(object):
    def setupUi(self, CadastroPedidoAtreladoDialog):
        CadastroPedidoAtreladoDialog.setObjectName("CadastroPedidoAtreladoDialog")
        CadastroPedidoAtreladoDialog.resize(820, 675)
        self.gridLayout = QtGui.QGridLayout(CadastroPedidoAtreladoDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_14 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.comissaoVendedorComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.comissaoVendedorComboBox.setObjectName("comissaoVendedorComboBox")
        self.horizontalLayout_10.addWidget(self.comissaoVendedorComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.comissaoDecoradorComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.comissaoDecoradorComboBox.setObjectName("comissaoDecoradorComboBox")
        self.horizontalLayout_13.addWidget(self.comissaoDecoradorComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.comissaoGerenteComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.comissaoGerenteComboBox.setObjectName("comissaoGerenteComboBox")
        self.horizontalLayout_14.addWidget(self.comissaoGerenteComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.vendedorComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.vendedorComboBox.setObjectName("vendedorComboBox")
        self.horizontalLayout_15.addWidget(self.vendedorComboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.lojaComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.lojaComboBox.setObjectName("lojaComboBox")
        self.horizontalLayout_12.addWidget(self.lojaComboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.tipoVendaComboBox = QtGui.QComboBox(CadastroPedidoAtreladoDialog)
        self.tipoVendaComboBox.setObjectName("tipoVendaComboBox")
        self.horizontalLayout_11.addWidget(self.tipoVendaComboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.valorTotalLineEdit = QtGui.QLineEdit(CadastroPedidoAtreladoDialog)
        self.valorTotalLineEdit.setObjectName("valorTotalLineEdit")
        self.horizontalLayout_6.addWidget(self.valorTotalLineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.dataVendaDateEdit = QtGui.QDateEdit(CadastroPedidoAtreladoDialog)
        self.dataVendaDateEdit.setObjectName("dataVendaDateEdit")
        self.horizontalLayout_7.addWidget(self.dataVendaDateEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.tableView = QtGui.QTableView(CadastroPedidoAtreladoDialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_6.addWidget(self.tableView)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_8, 3, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.clientePLLineEdit = QtGui.QLineEdit(CadastroPedidoAtreladoDialog)
        self.clientePLLineEdit.setReadOnly(True)
        self.clientePLLineEdit.setObjectName("clientePLLineEdit")
        self.horizontalLayout_2.addWidget(self.clientePLLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.vendedorPLLineEdit = QtGui.QLineEdit(CadastroPedidoAtreladoDialog)
        self.vendedorPLLineEdit.setReadOnly(True)
        self.vendedorPLLineEdit.setObjectName("vendedorPLLineEdit")
        self.horizontalLayout_3.addWidget(self.vendedorPLLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lojaPLLineEdit = QtGui.QLineEdit(CadastroPedidoAtreladoDialog)
        self.lojaPLLineEdit.setReadOnly(True)
        self.lojaPLLineEdit.setObjectName("lojaPLLineEdit")
        self.horizontalLayout_4.addWidget(self.lojaPLLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dataVendaPLDateEdit = QtGui.QDateEdit(CadastroPedidoAtreladoDialog)
        self.dataVendaPLDateEdit.setReadOnly(True)
        self.dataVendaPLDateEdit.setObjectName("dataVendaPLDateEdit")
        self.horizontalLayout_5.addWidget(self.dataVendaPLDateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.line = QtGui.QFrame(CadastroPedidoAtreladoDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(CadastroPedidoAtreladoDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pedidoPLLineEdit = QtGui.QLineEdit(CadastroPedidoAtreladoDialog)
        self.pedidoPLLineEdit.setObjectName("pedidoPLLineEdit")
        self.horizontalLayout.addWidget(self.pedidoPLLineEdit)
        self.pesquisarPushButton = QtGui.QPushButton(CadastroPedidoAtreladoDialog)
        self.pesquisarPushButton.setAutoDefault(False)
        self.pesquisarPushButton.setDefault(False)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.horizontalLayout.addWidget(self.pesquisarPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.cadastrarPushButton = QtGui.QPushButton(CadastroPedidoAtreladoDialog)
        self.cadastrarPushButton.setObjectName("cadastrarPushButton")
        self.gridLayout.addWidget(self.cadastrarPushButton, 4, 0, 1, 1)

        self.retranslateUi(CadastroPedidoAtreladoDialog)
        QtCore.QMetaObject.connectSlotsByName(CadastroPedidoAtreladoDialog)

    def retranslateUi(self, CadastroPedidoAtreladoDialog):
        CadastroPedidoAtreladoDialog.setWindowTitle(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Pedido Texguard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Comissão Vendedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Comissão Decorador", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Comissão Gerente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Vendedor Teflon:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Loja:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Tipo de Venda:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Valor total:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Data Venda Teflon:", None, QtGui.QApplication.UnicodeUTF8))
        self.dataVendaDateEdit.setDisplayFormat(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "d/M/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Produtos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Pedido Prima Linea", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Vendedor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Loja:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Data venda:", None, QtGui.QApplication.UnicodeUTF8))
        self.dataVendaPLDateEdit.setDisplayFormat(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "d/M/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Pedido Prima Linea:", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.cadastrarPushButton.setText(QtGui.QApplication.translate("CadastroPedidoAtreladoDialog", "Cadastrar", None, QtGui.QApplication.UnicodeUTF8))

