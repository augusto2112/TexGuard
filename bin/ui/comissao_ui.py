# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comissao.ui'
#
# Created: Thu May  5 16:18:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ComissaoWidget(object):
    def setupUi(self, ComissaoWidget):
        ComissaoWidget.setObjectName("ComissaoWidget")
        ComissaoWidget.resize(885, 568)
        self.gridLayout = QtGui.QGridLayout(ComissaoWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vendedorCheckBox = QtGui.QCheckBox(ComissaoWidget)
        self.vendedorCheckBox.setObjectName("vendedorCheckBox")
        self.horizontalLayout_5.addWidget(self.vendedorCheckBox)
        self.vendedorLineEdit = QtGui.QLineEdit(ComissaoWidget)
        self.vendedorLineEdit.setObjectName("vendedorLineEdit")
        self.horizontalLayout_5.addWidget(self.vendedorLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pedidoCheckBox = QtGui.QCheckBox(ComissaoWidget)
        self.pedidoCheckBox.setObjectName("pedidoCheckBox")
        self.horizontalLayout_6.addWidget(self.pedidoCheckBox)
        self.pedidoLineEdit = QtGui.QLineEdit(ComissaoWidget)
        self.pedidoLineEdit.setObjectName("pedidoLineEdit")
        self.horizontalLayout_6.addWidget(self.pedidoLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dataCheckBox = QtGui.QCheckBox(ComissaoWidget)
        self.dataCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataCheckBox.setObjectName("dataCheckBox")
        self.horizontalLayout_4.addWidget(self.dataCheckBox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(ComissaoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dataInicialDateEdit = QtGui.QDateEdit(ComissaoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataInicialDateEdit.sizePolicy().hasHeightForWidth())
        self.dataInicialDateEdit.setSizePolicy(sizePolicy)
        self.dataInicialDateEdit.setObjectName("dataInicialDateEdit")
        self.horizontalLayout_2.addWidget(self.dataInicialDateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(ComissaoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dataFinalDateEdit = QtGui.QDateEdit(ComissaoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFinalDateEdit.sizePolicy().hasHeightForWidth())
        self.dataFinalDateEdit.setSizePolicy(sizePolicy)
        self.dataFinalDateEdit.setObjectName("dataFinalDateEdit")
        self.horizontalLayout.addWidget(self.dataFinalDateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lojaCheckBox = QtGui.QCheckBox(ComissaoWidget)
        self.lojaCheckBox.setObjectName("lojaCheckBox")
        self.horizontalLayout_3.addWidget(self.lojaCheckBox)
        self.lojaComboBox = QtGui.QComboBox(ComissaoWidget)
        self.lojaComboBox.setObjectName("lojaComboBox")
        self.horizontalLayout_3.addWidget(self.lojaComboBox)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pesquisarPushButton = QtGui.QPushButton(ComissaoWidget)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.verticalLayout.addWidget(self.pesquisarPushButton)
        self.aplicarPushButton = QtGui.QPushButton(ComissaoWidget)
        self.aplicarPushButton.setObjectName("aplicarPushButton")
        self.verticalLayout.addWidget(self.aplicarPushButton)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.tableView = QtGui.QTableView(ComissaoWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(ComissaoWidget)
        QtCore.QMetaObject.connectSlotsByName(ComissaoWidget)

    def retranslateUi(self, ComissaoWidget):
        ComissaoWidget.setWindowTitle(QtGui.QApplication.translate("ComissaoWidget", "Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.vendedorCheckBox.setText(QtGui.QApplication.translate("ComissaoWidget", "Vendedor:", None, QtGui.QApplication.UnicodeUTF8))
        self.pedidoCheckBox.setText(QtGui.QApplication.translate("ComissaoWidget", "Pedido:", None, QtGui.QApplication.UnicodeUTF8))
        self.dataCheckBox.setText(QtGui.QApplication.translate("ComissaoWidget", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ComissaoWidget", "Data Inicial: ", None, QtGui.QApplication.UnicodeUTF8))
        self.dataInicialDateEdit.setDisplayFormat(QtGui.QApplication.translate("ComissaoWidget", "dd/MM/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ComissaoWidget", "Data Final: ", None, QtGui.QApplication.UnicodeUTF8))
        self.dataFinalDateEdit.setDisplayFormat(QtGui.QApplication.translate("ComissaoWidget", "dd/MM/yy", None, QtGui.QApplication.UnicodeUTF8))
        self.lojaCheckBox.setText(QtGui.QApplication.translate("ComissaoWidget", "Loja:", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("ComissaoWidget", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("ComissaoWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.aplicarPushButton.setText(QtGui.QApplication.translate("ComissaoWidget", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.aplicarPushButton.setShortcut(QtGui.QApplication.translate("ComissaoWidget", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))

