# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_Inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.cadastrar_se_botao = QtWidgets.QPushButton(self.frame_2)
        self.cadastrar_se_botao.setGeometry(QtCore.QRect(160, 170, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cadastrar_se_botao.setFont(font)
        self.cadastrar_se_botao.setMouseTracking(False)
        self.cadastrar_se_botao.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.cadastrar_se_botao.setObjectName("cadastrar_se_botao")
        self.login_botao = QtWidgets.QPushButton(self.frame_2)
        self.login_botao.setGeometry(QtCore.QRect(460, 170, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.login_botao.setFont(font)
        self.login_botao.setMouseTracking(True)
        self.login_botao.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.login_botao.setObjectName("login_botao")
        self.LEBANK_label = QtWidgets.QLabel(self.frame_2)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio"))
        self.cadastrar_se_botao.setText(_translate("MainWindow", "CADASTRE-SE"))
        self.login_botao.setText(_translate("MainWindow", "LOGIN"))
        self.LEBANK_label.setText(_translate("MainWindow", "                                                 LEBANK"))

