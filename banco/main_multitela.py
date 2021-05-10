import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from banco import Cliente, Historico, Conta
from tela_inicial import Tela_Inicial
from tela_de_cadastro import Tela_Cadastro
from tela_de_depositar import Tela_Deposito
from tela_de_extrato import Tela_Extrato
from tela_de_login import Tela_Login
from tela_de_saque import Tela_Saque
from tela_de_transferir import Tela_Transferencia
from tela_principal import Tela_Principal


class Ui_Main(QtWidgets.QWidget):
    def setupUI(self, Main):
        Main.setObjectName('Main')
        Main.resize(800, 600)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_depositar = Tela_Deposito()
        self.tela_depositar.setupUi(self.stack2)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack3)

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack4)

        self.tela_saque = Tela_Saque()
        self.tela_saque.setupUi(self.stack5)

        self.tela_transferir = Tela_Transferencia()
        self.tela_transferir.setupUi(self.stack6)

        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


