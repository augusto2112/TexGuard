# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created: Thu May  5 16:18:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ClienteWidget(object):
    def setupUi(self, ClienteWidget):
        ClienteWidget.setObjectName("ClienteWidget")
        ClienteWidget.resize(463, 361)
        self.gridLayout = QtGui.QGridLayout(ClienteWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nomeRadioButton = QtGui.QRadioButton(ClienteWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomeRadioButton.sizePolicy().hasHeightForWidth())
        self.nomeRadioButton.setSizePolicy(sizePolicy)
        self.nomeRadioButton.setChecked(True)
        self.nomeRadioButton.setObjectName("nomeRadioButton")
        self.horizontalLayout_4.addWidget(self.nomeRadioButton)
        self.codigoRadioButton = QtGui.QRadioButton(ClienteWidget)
        self.codigoRadioButton.setChecked(False)
        self.codigoRadioButton.setObjectName("codigoRadioButton")
        self.horizontalLayout_4.addWidget(self.codigoRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtGui.QLineEdit(ClienteWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.pesquisarPushButton = QtGui.QPushButton(ClienteWidget)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.horizontalLayout_6.addWidget(self.pesquisarPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableView = QtGui.QTableView(ClienteWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        self.retranslateUi(ClienteWidget)
        QtCore.QMetaObject.connectSlotsByName(ClienteWidget)

    def retranslateUi(self, ClienteWidget):
        ClienteWidget.setWindowTitle(QtGui.QApplication.translate("ClienteWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeRadioButton.setText(QtGui.QApplication.translate("ClienteWidget", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.codigoRadioButton.setText(QtGui.QApplication.translate("ClienteWidget", "Código", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("ClienteWidget", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("ClienteWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))

