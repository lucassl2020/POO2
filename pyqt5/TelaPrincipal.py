# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class TelaPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buscar_botao = QtWidgets.QPushButton(self.centralwidget)
        self.buscar_botao.setGeometry(QtCore.QRect(390, 100, 91, 31))
        self.buscar_botao.setObjectName("buscar_botao")
        self.cadastrar_botao = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrar_botao.setGeometry(QtCore.QRect(50, 100, 91, 31))
        self.cadastrar_botao.setObjectName("cadastrar_botao")
        self.opcoes_label = QtWidgets.QLabel(self.centralwidget)
        self.opcoes_label.setGeometry(QtCore.QRect(190, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.opcoes_label.setFont(font)
        self.opcoes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.opcoes_label.setObjectName("opcoes_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuFile.addAction(self.actionSair)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela principal"))
        self.buscar_botao.setText(_translate("MainWindow", "Buscar"))
        self.cadastrar_botao.setText(_translate("MainWindow", "Cadastrar"))
        self.opcoes_label.setText(_translate("MainWindow", "Opções"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))

