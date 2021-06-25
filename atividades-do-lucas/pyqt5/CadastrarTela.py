# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrarTela.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class CadastrarTela(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 298)
        self.cadastrar_background = QtWidgets.QLabel(Form)
        self.cadastrar_background.setEnabled(True)
        self.cadastrar_background.setGeometry(QtCore.QRect(60, 50, 481, 211))
        self.cadastrar_background.setSizeIncrement(QtCore.QSize(0, 0))
        self.cadastrar_background.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_background.setStyleSheet("background: #6C76EF;\n"
"border-radius: 12px;")
        self.cadastrar_background.setLineWidth(1)
        self.cadastrar_background.setText("")
        self.cadastrar_background.setObjectName("cadastrar_background")
        self.nome_label = QtWidgets.QLabel(Form)
        self.nome_label.setGeometry(QtCore.QRect(70, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;\n"
"\n"
"")
        self.nome_label.setObjectName("nome_label")
        self.nome_line = QtWidgets.QLineEdit(Form)
        self.nome_line.setGeometry(QtCore.QRect(200, 70, 331, 20))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.nome_line.setFont(font)
        self.nome_line.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nome_line.setAutoFillBackground(False)
        self.nome_line.setStyleSheet("border-radius:5px;")
        self.nome_line.setObjectName("nome_line")
        self.cpf_line = QtWidgets.QLineEdit(Form)
        self.cpf_line.setGeometry(QtCore.QRect(200, 130, 141, 20))
        self.cpf_line.setStyleSheet("border-radius:5px;")
        self.cpf_line.setObjectName("cpf_line")
        self.cpf_label = QtWidgets.QLabel(Form)
        self.cpf_label.setGeometry(QtCore.QRect(70, 130, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpf_label.setFont(font)
        self.cpf_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;")
        self.cpf_label.setObjectName("cpf_label")
        self.endereco_label = QtWidgets.QLabel(Form)
        self.endereco_label.setGeometry(QtCore.QRect(70, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endereco_label.setFont(font)
        self.endereco_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;")
        self.endereco_label.setObjectName("endereco_label")
        self.endereco_line = QtWidgets.QLineEdit(Form)
        self.endereco_line.setGeometry(QtCore.QRect(200, 100, 331, 20))
        self.endereco_line.setStyleSheet("border-radius:5px;")
        self.endereco_line.setObjectName("endereco_line")
        self.data_nascimento_label = QtWidgets.QLabel(Form)
        self.data_nascimento_label.setGeometry(QtCore.QRect(70, 160, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_nascimento_label.setFont(font)
        self.data_nascimento_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;")
        self.data_nascimento_label.setObjectName("data_nascimento_label")
        self.data_nascimento_line = QtWidgets.QLineEdit(Form)
        self.data_nascimento_line.setGeometry(QtCore.QRect(200, 160, 141, 20))
        self.data_nascimento_line.setSizeIncrement(QtCore.QSize(4, 0))
        self.data_nascimento_line.setStyleSheet("border-radius:5px;")
        self.data_nascimento_line.setObjectName("data_nascimento_line")
        self.cadastrar_botao = QtWidgets.QPushButton(Form)
        self.cadastrar_botao.setGeometry(QtCore.QRect(260, 220, 81, 31))
        self.cadastrar_botao.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);  \n"
"  background-color: rgb(176, 185, 239);\n"
"  border: none;\n"
"  opacity: 0.6;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  opacity: 1\n"
"}\n"
"")
        self.cadastrar_botao.setObjectName("cadastrar_botao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastra"))
        self.nome_label.setText(_translate("Form", "Nome"))
        self.cpf_label.setText(_translate("Form", "CPF"))
        self.endereco_label.setText(_translate("Form", "Endereço"))
        self.data_nascimento_label.setText(_translate("Form", "Data de Nascimento"))
        self.cadastrar_botao.setText(_translate("Form", "Cadastrar"))

