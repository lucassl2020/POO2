# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_de_depositar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_Deposito(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 101))
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
        self.saldo_label = QtWidgets.QLabel(self.frame)
        self.saldo_label.setGeometry(QtCore.QRect(580, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saldo_label.setFont(font)
        self.saldo_label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(19, 11, 98);")
        self.saldo_label.setObjectName("saldo_label")
        self.saldo_line = QtWidgets.QLineEdit(self.frame)
        self.saldo_line.setGeometry(QtCore.QRect(630, 30, 141, 21))
        self.saldo_line.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(23, 14, 121);")
        self.saldo_line.setObjectName("saldo_line")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 811, 271))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.valor_a_ser_depositado_line = QtWidgets.QLineEdit(self.frame_2)
        self.valor_a_ser_depositado_line.setGeometry(QtCore.QRect(290, 70, 221, 20))
        self.valor_a_ser_depositado_line.setObjectName("valor_a_ser_depositado_line")
        self.valor_a_ser_depositado_label = QtWidgets.QLabel(self.frame_2)
        self.valor_a_ser_depositado_label.setGeometry(QtCore.QRect(110, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valor_a_ser_depositado_label.setFont(font)
        self.valor_a_ser_depositado_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor_a_ser_depositado_label.setObjectName("valor_a_ser_depositado_label")
        self.confirmar_botao = QtWidgets.QPushButton(self.frame_2)
        self.confirmar_botao.setGeometry(QtCore.QRect(110, 140, 211, 51))
        self.confirmar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.confirmar_botao.setObjectName("confirmar_botao")
        self.voltar_botao = QtWidgets.QPushButton(self.frame_2)
        self.voltar_botao.setGeometry(QtCore.QRect(420, 140, 211, 51))
        self.voltar_botao.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.voltar_botao.setObjectName("voltar_botao")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 370, 811, 201))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deposito"))
        self.LEBANK_label.setText(_translate("MainWindow", "                                                 LEBANK"))
        self.saldo_label.setText(_translate("MainWindow", "Saldo:"))
        self.valor_a_ser_depositado_label.setText(_translate("MainWindow", "Valor à ser depositado:"))
        self.confirmar_botao.setText(_translate("MainWindow", "CONFIRMAR"))
        self.voltar_botao.setText(_translate("MainWindow", "VOLTAR"))

