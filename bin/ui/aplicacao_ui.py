# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aplicacao.ui'
#
# Created: Thu May  5 16:18:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AplicacaoWidget(object):
    def setupUi(self, AplicacaoWidget):
        AplicacaoWidget.setObjectName("AplicacaoWidget")
        AplicacaoWidget.resize(612, 440)
        self.gridLayout = QtGui.QGridLayout(AplicacaoWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pedidoTeflonCheckBox = QtGui.QCheckBox(AplicacaoWidget)
        self.pedidoTeflonCheckBox.setObjectName("pedidoTeflonCheckBox")
        self.horizontalLayout.addWidget(self.pedidoTeflonCheckBox)
        self.pedidoTeflonLineEdit = QtGui.QLineEdit(AplicacaoWidget)
        self.pedidoTeflonLineEdit.setObjectName("pedidoTeflonLineEdit")
        self.horizontalLayout.addWidget(self.pedidoTeflonLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pedidoPLCheckBox = QtGui.QCheckBox(AplicacaoWidget)
        self.pedidoPLCheckBox.setObjectName("pedidoPLCheckBox")
        self.horizontalLayout_2.addWidget(self.pedidoPLCheckBox)
        self.pedidoPLLineEdit = QtGui.QLineEdit(AplicacaoWidget)
        self.pedidoPLLineEdit.setObjectName("pedidoPLLineEdit")
        self.horizontalLayout_2.addWidget(self.pedidoPLLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.codProdutoCheckBox = QtGui.QCheckBox(AplicacaoWidget)
        self.codProdutoCheckBox.setObjectName("codProdutoCheckBox")
        self.horizontalLayout_6.addWidget(self.codProdutoCheckBox)
        self.codProdutoLineEdit = QtGui.QLineEdit(AplicacaoWidget)
        self.codProdutoLineEdit.setObjectName("codProdutoLineEdit")
        self.horizontalLayout_6.addWidget(self.codProdutoLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.pesquisarPushButton = QtGui.QPushButton(AplicacaoWidget)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.horizontalLayout_4.addWidget(self.pesquisarPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tableView = QtGui.QTableView(AplicacaoWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(AplicacaoWidget)
        QtCore.QMetaObject.connectSlotsByName(AplicacaoWidget)

    def retranslateUi(self, AplicacaoWidget):
        AplicacaoWidget.setWindowTitle(QtGui.QApplication.translate("AplicacaoWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pedidoTeflonCheckBox.setText(QtGui.QApplication.translate("AplicacaoWidget", "Pedido Teflon:", None, QtGui.QApplication.UnicodeUTF8))
        self.pedidoPLCheckBox.setText(QtGui.QApplication.translate("AplicacaoWidget", "Pedido Prima Linea:", None, QtGui.QApplication.UnicodeUTF8))
        self.codProdutoCheckBox.setText(QtGui.QApplication.translate("AplicacaoWidget", "Código Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("AplicacaoWidget", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("AplicacaoWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))

