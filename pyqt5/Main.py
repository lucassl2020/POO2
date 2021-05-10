from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cadastro import Pessoa, Cadastro
from TelaPrincipal import TelaPrincipal
from CadastrarTela import CadastrarTela
from BuscarTela import BuscarTela
import sys

class MainUi(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.inicial_tela = TelaPrincipal()
        self.inicial_tela.setupUi(self.stack0)

        self.cadastrar_tela = CadastrarTela()
        self.cadastrar_tela.setupUi(self.stack1)

        self.buscar_tela = BuscarTela()
        self.buscar_tela.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

        
class Main(QtWidgets.QMainWindow, MainUi):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.inicial_tela.cadastrar_botao.clicked.connect(self.cadastrarAbrirTela)
        self.inicial_tela.buscar_botao.clicked.connect(self.buscarAbrirTela)

        self.cadastrar_tela.cadastrar_botao.clicked.connect(self.botaoCadastra)
        self.buscar_tela.buscar_botao.clicked.connect(self.botaoBusca)

        self.buscar_tela.voltar_botao.clicked.connect(self.botaoVoltar)

    def cadastrarAbrirTela(self):
        self.QtStack.setCurrentIndex(1)

    def buscarAbrirTela(self):
        self.QtStack.setCurrentIndex(2)

    def botaoCadastra(self):
        nome = self.cadastrar_tela.nome_line.text()
        endereco = self.cadastrar_tela.endereco_line.text()
        cpf = self.cadastrar_tela.cpf_line.text()
        nascimento = self.cadastrar_tela.data_nascimento_line.text()

        if nome != "" and endereco != "" and cpf != "" and nascimento != "":
            pessoa = Pessoa(nome, endereco, cpf, nascimento)
            if self.cad.cadastra(pessoa):
                QMessageBox.information(None, "POO2", "Cadastro realizado")
                self.cadastrar_tela.nome_line.setText("")
                self.cadastrar_tela.endereco_line.setText("")
                self.cadastrar_tela.cpf_line.setText("")
                self.cadastrar_tela.data_nascimento_line.setText("")

                self.QtStack.setCurrentIndex(0)
            else:
                QMessageBox.information(None, "POO2", "O cpf ja existe")
        else:
            QMessageBox.information(None, "POO2", "Todas as informações devem ser preenchidas")


    def botaoBusca(self):
        cpf = self.buscar_tela.cpf_line.text()
        pessoa = self.cad.busca(cpf)

        if pessoa:
            self.buscar_tela.nome_line.setText(pessoa.nome)
            self.buscar_tela.endereco_line.setText(pessoa.endereco)
            self.buscar_tela.data_nascimento_line.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, "POO2", "Cpf não encontrado")

    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)

            
if __name__ == "__main__":
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
