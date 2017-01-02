# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'endereco.ui'
#
# Created: Thu May  5 16:18:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EnderecoWidget(object):
    def setupUi(self, EnderecoWidget):
        EnderecoWidget.setObjectName("EnderecoWidget")
        EnderecoWidget.resize(608, 436)
        self.gridLayout = QtGui.QGridLayout(EnderecoWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nomeClienteRadioButton = QtGui.QRadioButton(EnderecoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomeClienteRadioButton.sizePolicy().hasHeightForWidth())
        self.nomeClienteRadioButton.setSizePolicy(sizePolicy)
        self.nomeClienteRadioButton.setChecked(True)
        self.nomeClienteRadioButton.setObjectName("nomeClienteRadioButton")
        self.horizontalLayout.addWidget(self.nomeClienteRadioButton)
        self.codigoClienteRadioButton = QtGui.QRadioButton(EnderecoWidget)
        self.codigoClienteRadioButton.setChecked(False)
        self.codigoClienteRadioButton.setObjectName("codigoClienteRadioButton")
        self.horizontalLayout.addWidget(self.codigoClienteRadioButton)
        self.enderecoRadioButton = QtGui.QRadioButton(EnderecoWidget)
        self.enderecoRadioButton.setObjectName("enderecoRadioButton")
        self.horizontalLayout.addWidget(self.enderecoRadioButton)
        self.cidadeRadioButton = QtGui.QRadioButton(EnderecoWidget)
        self.cidadeRadioButton.setObjectName("cidadeRadioButton")
        self.horizontalLayout.addWidget(self.cidadeRadioButton)
        self.ufRadioButton = QtGui.QRadioButton(EnderecoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ufRadioButton.sizePolicy().hasHeightForWidth())
        self.ufRadioButton.setSizePolicy(sizePolicy)
        self.ufRadioButton.setObjectName("ufRadioButton")
        self.horizontalLayout.addWidget(self.ufRadioButton)
        self.codEnderecoRadioButton = QtGui.QRadioButton(EnderecoWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codEnderecoRadioButton.sizePolicy().hasHeightForWidth())
        self.codEnderecoRadioButton.setSizePolicy(sizePolicy)
        self.codEnderecoRadioButton.setObjectName("codEnderecoRadioButton")
        self.horizontalLayout.addWidget(self.codEnderecoRadioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtGui.QLineEdit(EnderecoWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.pesquisarPushButton = QtGui.QPushButton(EnderecoWidget)
        self.pesquisarPushButton.setObjectName("pesquisarPushButton")
        self.horizontalLayout_6.addWidget(self.pesquisarPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.tableView = QtGui.QTableView(EnderecoWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 1)

        self.retranslateUi(EnderecoWidget)
        QtCore.QMetaObject.connectSlotsByName(EnderecoWidget)

    def retranslateUi(self, EnderecoWidget):
        EnderecoWidget.setWindowTitle(QtGui.QApplication.translate("EnderecoWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeClienteRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Nome Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.codigoClienteRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Código Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.enderecoRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Endereço", None, QtGui.QApplication.UnicodeUTF8))
        self.cidadeRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Cidade", None, QtGui.QApplication.UnicodeUTF8))
        self.ufRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "UF", None, QtGui.QApplication.UnicodeUTF8))
        self.codEnderecoRadioButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Código Endereco", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setText(QtGui.QApplication.translate("EnderecoWidget", "Pesquisar", None, QtGui.QApplication.UnicodeUTF8))
        self.pesquisarPushButton.setShortcut(QtGui.QApplication.translate("EnderecoWidget", "Return", None, QtGui.QApplication.UnicodeUTF8))

