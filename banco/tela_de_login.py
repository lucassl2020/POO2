# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_de_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 151))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LEBANK_label = QtWidgets.QLabel(self.frame)
        self.LEBANK_label.setGeometry(QtCore.QRect(0, 0, 811, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(16)
        self.LEBANK_label.setFont(font)
        self.LEBANK_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LEBANK_label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.LEBANK_label.setObjectName("LEBANK_label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 150, 811, 211))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.numero_da_conta_line = QtWidgets.QLineEdit(self.frame_2)
        self.numero_da_conta_line.setGeometry(QtCore.QRect(240, 30, 391, 20))
        self.numero_da_conta_line.setObjectName("numero_da_conta_line")
        self.numero_da_conta_label = QtWidgets.QLabel(self.frame_2)
        self.numero_da_conta_label.setGeometry(QtCore.QRect(70, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numero_da_conta_label.setFont(font)
        self.numero_da_conta_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numero_da_conta_label.setObjectName("numero_da_conta_label")
        self.senha_label = QtWidgets.QLabel(self.frame_2)
        self.senha_label.setGeometry(QtCore.QRect(150, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.senha_label.setFont(font)
        self.senha_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senha_label.setObjectName("senha_label")
        self.senha_line = QtWidgets.QLineEdit(self.frame_2)
        self.senha_line.setGeometry(QtCore.QRect(240, 90, 391, 20))
        self.senha_line.setObjectName("senha_line")
        self.logar_botao = QtWidgets.QPushButton(self.frame_2)
        self.logar_botao.setGeometry(QtCore.QRect(120, 140, 211, 51))
        self.logar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.logar_botao.setObjectName("logar_botao")
        self.voltar_botao = QtWidgets.QPushButton(self.frame_2)
        self.voltar_botao.setGeometry(QtCore.QRect(510, 140, 211, 51))
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.voltar_botao.setObjectName("voltar_botao")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-10, 370, 811, 221))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.LEBANK_label.setText(_translate("MainWindow", "                                                 LEBANK"))
        self.numero_da_conta_label.setText(_translate("MainWindow", "Número da conta:"))
        self.senha_label.setText(_translate("MainWindow", "Senha:"))
        self.logar_botao.setText(_translate("MainWindow", "Logar"))
        self.voltar_botao.setText(_translate("MainWindow", "Voltar"))

