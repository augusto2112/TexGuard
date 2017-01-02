# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'produto.ui'
#
# Created: Thu May  5 16:18:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProdutoWidget(object):
    def setupUi(self, ProdutoWidget):
        ProdutoWidget.setObjectName("ProdutoWidget")
        ProdutoWidget.resize(716, 473)
        self.gridLayout = QtGui.QGridLayout(ProdutoWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pedidoPLCheckBox = QtGui.QCheckBox(ProdutoWidget)
        self.pedidoPLCheckBox.setObjectName("pedidoPLCheckBox")
        self.horizontalLayout.addWidget(self.pedidoPLCheckBox)
        self.pedidoLineEdit = QtGui.QLineEdit(ProdutoWidget)
        self.pedidoLineEdit.setObjectName("pedidoLineEdit")
        self.horizontalLayout.addWidget(self.pedidoLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.codProdutoCheckBox = QtGui.QCheckBox(ProdutoWidget)
        self.codProdutoCheckBox.setObjectName("codProdutoCheckBox")
        self.horizontalLayout_3.addWidget(self.codProdutoCheckBox)
        self.codProdutoLineEdit = QtGui.QLineEdit(ProdutoWidget)
        self.codProdutoLineEdit.setObjectName("codProdutoLineEdit")
        self.horizontalLayout_3.addWidget(self.codProdutoLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vendeuTeflonCheckBox = QtGui.QCheckBox(ProdutoWidget)
        self.vendeuTeflonCheckBox.setObjectName("vendeuTeflonCheckBox")
        self.horizontalLayout_2.addWidget(self.vendeuTeflonCheckBox)
        self.vendeuTeflonComboBox = QtGui.QComboBox(ProdutoWidget)
        self.vendeuTeflonComboBox.setObjectName("vendeuTeflonComboBox")
        self.horizontalLayout_2.addWidget(self.vendeuTeflonComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pesquisarPushButton = QtGui.QPushButton(ProdutoWidget)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.verticalLayout_2.addWidget(self.pesquisarPushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tableView = QtGui.QTableView(ProdutoWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(ProdutoWidget)
        QtCore.QMetaObject.connectSlotsByName(ProdutoWidget)

    def retranslateUi(self, ProdutoWidget):
        ProdutoWidget.setWindowTitle(QtGui.QApplication.translate("ProdutoWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pedidoPLCheckBox.setText(QtGui.QApplication.translate("ProdutoWidget", "Pedido PL:", None, QtGui.QApplication.UnicodeUTF8))
        self.codProdutoCheckBox.setText(QtGui.QApplication.translate("ProdutoWidget", "Código Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.vendeuTeflonCheckBox.setText(QtGui.QApplication.translate("ProdutoWidget", "Vendeu Teflon", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("ProdutoWidget", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("ProdutoWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))

