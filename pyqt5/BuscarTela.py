# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscarTela.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class BuscarTela(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 308)
        self.buscar_background = QtWidgets.QLabel(Form)
        self.buscar_background.setEnabled(True)
        self.buscar_background.setGeometry(QtCore.QRect(50, 30, 481, 241))
        self.buscar_background.setStyleSheet("background: #6C76EF;\n"
"border-radius: 12px;")
        self.buscar_background.setText("")
        self.buscar_background.setObjectName("buscar_background")
        self.data_nascimento_line = QtWidgets.QLineEdit(Form)
        self.data_nascimento_line.setGeometry(QtCore.QRect(190, 240, 141, 20))
        self.data_nascimento_line.setStyleSheet("border-radius:5px;")
        self.data_nascimento_line.setObjectName("data_nascimento_line")
        self.endereco_line = QtWidgets.QLineEdit(Form)
        self.endereco_line.setGeometry(QtCore.QRect(190, 210, 331, 20))
        self.endereco_line.setStyleSheet("border-radius:5px;")
        self.endereco_line.setObjectName("endereco_line")
        self.buscar_botao = QtWidgets.QPushButton(Form)
        self.buscar_botao.setGeometry(QtCore.QRect(200, 100, 81, 31))
        self.buscar_botao.setStyleSheet("QPushButton {\n"
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
        self.buscar_botao.setObjectName("buscar_botao")
        self.cpf_line = QtWidgets.QLineEdit(Form)
        self.cpf_line.setGeometry(QtCore.QRect(190, 40, 141, 20))
        self.cpf_line.setStyleSheet("border-radius:5px;")
        self.cpf_line.setObjectName("cpf_line")
        self.endereco_label = QtWidgets.QLabel(Form)
        self.endereco_label.setGeometry(QtCore.QRect(60, 210, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endereco_label.setFont(font)
        self.endereco_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;\n"
"\n"
"")
        self.endereco_label.setObjectName("endereco_label")
        self.cpf_label = QtWidgets.QLabel(Form)
        self.cpf_label.setGeometry(QtCore.QRect(60, 40, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpf_label.setFont(font)
        self.cpf_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;\n"
"\n"
"")
        self.cpf_label.setObjectName("cpf_label")
        self.nome_label = QtWidgets.QLabel(Form)
        self.nome_label.setGeometry(QtCore.QRect(60, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;\n"
"\n"
"")
        self.nome_label.setObjectName("nome_label")
        self.data_nascimento_label = QtWidgets.QLabel(Form)
        self.data_nascimento_label.setGeometry(QtCore.QRect(60, 240, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_nascimento_label.setFont(font)
        self.data_nascimento_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: #6C76EF;\n"
"\n"
"")
        self.data_nascimento_label.setObjectName("data_nascimento_label")
        self.nome_line = QtWidgets.QLineEdit(Form)
        self.nome_line.setGeometry(QtCore.QRect(190, 180, 331, 20))
        self.nome_line.setStyleSheet("border-radius:5px;")
        self.nome_line.setObjectName("nome_line")
        self.voltar_botao = QtWidgets.QPushButton(Form)
        self.voltar_botao.setGeometry(QtCore.QRect(290, 100, 81, 31))
        self.voltar_botao.setStyleSheet("QPushButton {\n"
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
        self.voltar_botao.setObjectName("voltar_botao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Busca"))
        self.buscar_botao.setText(_translate("Form", "Buscar"))
        self.endereco_label.setText(_translate("Form", "Endereço"))
        self.cpf_label.setText(_translate("Form", "CPF"))
        self.nome_label.setText(_translate("Form", "Nome"))
        self.data_nascimento_label.setText(_translate("Form", "Data de Nascimento"))
        self.voltar_botao.setText(_translate("Form", "Voltar"))

