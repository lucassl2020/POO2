# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Principal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 61))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 811, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.210227 rgba(255, 255, 0, 255), stop:0.778409 rgba(255, 255, 117, 255));")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(580, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(19, 11, 98);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(630, 30, 141, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(23, 14, 121);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(19, 11, 98);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 30, 281, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(23, 14, 121);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-10, 60, 811, 451))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0681818 rgba(14, 8, 73, 255), stop:0.607955 rgba(28, 17, 145, 255));\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(150, 30, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 30, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 220, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 220, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 370, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(28, 17, 145);")
        self.pushButton_5.setObjectName("pushButton_5")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "                                                 LEBANK"))
        self.label.setText(_translate("MainWindow", "Saldo:"))
        self.label_2.setText(_translate("MainWindow", "Titular:"))
        self.pushButton.setText(_translate("MainWindow", "Ver extrato"))
        self.pushButton_2.setText(_translate("MainWindow", "Transferir"))
        self.pushButton_3.setText(_translate("MainWindow", "Sacar"))
        self.pushButton_4.setText(_translate("MainWindow", "Depositar"))
        self.pushButton_5.setText(_translate("MainWindow", "Sair"))
