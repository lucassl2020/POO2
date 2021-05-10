import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from banco import Banco
from Cliente import Cliente
from Conta import Conta
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

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)

        self.banco = Banco()
        self.tela_inicial.cadastrar_se_botao.clicked.connect(self.cadastrarAbrirTela)
        self.tela_inicial.login_botao.clicked.connect(self.loginAbrirTela)

        self.tela_cadastro.confirmar_botao.clicked.connect(self.cadastrarCliente)
        self.tela_cadastro.voltar_botao.clicked.connect(self.voltarTelaInicial)

        self.tela_login.logar_botao.clicked.connect(self.logarCliente)
        self.tela_login.voltar_botao.clicked.connect(self.voltarTelaInicial)

        self.tela_principal.sair_botao.clicked.connect(self.sairTelaPrincipal)
        self.tela_principal.ver_extrato_botao.clicked.connect(self.extratoAbrirTela)
        self.tela_principal.transferir_botao.clicked.connect(self.transferirAbrirTela)
        self.tela_principal.sacar_botao.clicked.connect(self.sacarAbrirTela)
        self.tela_principal.depositar_botao.clicked.connect(self.depositarAbrirTela)

        self.tela_extrato.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_transferir.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_saque.voltar_botao.clicked.connect(self.entrarTelaPrincipal)
        self.tela_depositar.voltar_botao.clicked.connect(self.entrarTelaPrincipal)

        self.tela_saque.confirmar_botao.clicked.connect(self.saqueConfirmar)
        self.tela_depositar.confirmar_botao.clicked.connect(self.depositoConfirmar)

        self.tela_transferir.transferir_botao.clicked.connect(self.transferirSaldo)
        self.tela_transferir.buscar_botao.clicked.connect(self.buscarDestinatario)

    def cadastrarAbrirTela(self):
        self.tela_cadastro.nome_line.setText('')
        self.tela_cadastro.sobrenome_line.setText('')
        self.tela_cadastro.cpf_line.setText('')
        self.tela_cadastro.senha_line.setText('')
        self.QtStack.setCurrentIndex(1)
        
    def loginAbrirTela(self):
        self.QtStack.setCurrentIndex(4)

    def cadastrarCliente(self):
        nome = self.tela_cadastro.nome_line.text()
        sobrenome = self.tela_cadastro.sobrenome_line.text()
        cpf = self.tela_cadastro.cpf_line.text()
        senha = self.tela_cadastro.senha_line.text()

        if nome != '' and sobrenome != '' and cpf != '' and senha != '':
            if cpf not in self.banco.clientes:
                cliente = Cliente(nome, sobrenome, cpf)
                if self.banco.clienteCadastrar(cliente):
                    conta = Conta(cliente, senha)
                    if self.banco.contaCadastrar(conta):
                        QMessageBox.information(None, "LEBANK", f"Cadastro feito com sucesso\n\nNumero da conta: {conta.numero}")
                        self.QtStack.setCurrentIndex(0)                    
                    else:
                        QMessageBox.information(None, "LEBANK", "Falha ao cadastrar dados do cliente")
                else:        
                    QMessageBox.information(None, "LEBANK", "Falha ao cadastrar dados do cliente")
            else:
                QMessageBox.information(None, "LEBANK", "O cpf ja esta cadastrado")
        else:
            QMessageBox.information(None, "LEBANK", "Preencha todos os campos")

    def voltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def logarCliente(self):
        numero_da_conta = self.tela_login.numero_da_conta_line.text()
        senha = self.tela_login.senha_line.text()

        if numero_da_conta != '' and senha != '':
            if self.banco.login(numero_da_conta, senha):
                self.tela_login.numero_da_conta_line.setText('')
                self.tela_login.senha_line.setText('')
                self.entrarTelaPrincipal()
            else:
                QMessageBox.information(None, "LEBANK", "Falha no login")
        else:
            QMessageBox.information(None, "LEBANK", "Preencha todos os campos")

    def entrarTelaPrincipal(self):
        self.QtStack.setCurrentIndex(7)
        self.tela_principal.titular_line.setText(self.banco.conta_atual.titular.nome + ' ' + self.banco.conta_atual.titular.sobrenome)
        self.tela_principal.saldo_line.setText(str(self.banco.conta_atual.saldo))

    def sairTelaPrincipal(self):
        self.banco.conta_atual = None
        self.QtStack.setCurrentIndex(4)

    def extratoAbrirTela(self):
        self.tela_extrato.numero_line.setText('')
        self.tela_extrato.titular_line.setText('')
        self.tela_extrato.saldo_line.setText('')
        self.tela_extrato.limite_line.setText('')
        self.tela_extrato.historico_line.setText('')

        self.QtStack.setCurrentIndex(3)

        self.tela_extrato.numero_line.setText(str(self.banco.conta_atual.numero))
        self.tela_extrato.titular_line.setText(self.banco.conta_atual.titular.nome + ' ' + self.banco.conta_atual.titular.sobrenome)
        self.tela_extrato.saldo_line.setText(str(self.banco.conta_atual.saldo))
        self.tela_extrato.limite_line.setText(str(self.banco.conta_atual.limite))
        self.tela_extrato.historico_line.setText(self.banco.conta_atual.extrato())

    def transferirAbrirTela(self):
        self.tela_transferir.saldo_line.setText(str(self.banco.conta_atual.saldo))
        self.tela_transferir.numero_da_conta_do_destinatario_line.setText('')
        self.tela_transferir.nome_do_destinatario_line.setText('')
        self.tela_transferir.cpf_do_destinatario_line.setText('')
        self.tela_transferir.valor_a_ser_transferido_line.setText('')

        self.QtStack.setCurrentIndex(6)

    def sacarAbrirTela(self):
        self.tela_saque.saldo_line.setText(str(self.banco.conta_atual.saldo))
        self.tela_saque.valor_a_ser_sacado_line.setText('')

        self.QtStack.setCurrentIndex(5)

    def saqueConfirmar(self):
        valor_a_ser_sacado = self.tela_saque.valor_a_ser_sacado_line.text()
        try:
            if valor_a_ser_sacado != '':
                if self.banco.conta_atual.saca(float(valor_a_ser_sacado.replace(',', '.'))):
                    QMessageBox.information(None, "LEBANK", "Saque realizado com sucesso")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido\nou\nMaior que o saldo")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha o campo")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def depositarAbrirTela(self):
        self.tela_depositar.saldo_line.setText(str(self.banco.conta_atual.saldo))
        self.tela_depositar.valor_a_ser_depositado_line.setText('')

        self.QtStack.setCurrentIndex(2)

    def depositoConfirmar(self):
        valor_a_ser_depositado = self.tela_depositar.valor_a_ser_depositado_line.text()
        try:
            if valor_a_ser_depositado != '':
                if self.banco.conta_atual.deposita(float(valor_a_ser_depositado.replace(',', '.'))):
                    QMessageBox.information(None, "LEBANK", "Deposito realizado com sucesso")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido\nou\nPassa do limite")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha o campo")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def transferirSaldo(self):
        numero_da_conta_do_destinatario = self.tela_transferir.numero_da_conta_do_destinatario_line.text()
        valor_a_ser_transferido = self.tela_transferir.valor_a_ser_transferido_line.text()

        conta_destinatario = self.banco.contas[numero_da_conta_do_destinatario]

        try:
            if numero_da_conta_do_destinatario != '' and valor_a_ser_transferido != '':
                if self.banco.conta_atual.transfere(conta_destinatario, float(valor_a_ser_transferido.replace(',', '.'))):
                    QMessageBox.information(None, "LEBANK", "Transferencia realizada com sucesso\n")
                    self.entrarTelaPrincipal()
                else:
                    QMessageBox.information(None, "LEBANK", "Valor invalido")
            else:
                QMessageBox.information(None, "LEBANK", "Preencha os campos necessarios")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")

    def buscarDestinatario(self):
        numero_da_conta_do_destinatario = self.tela_transferir.numero_da_conta_do_destinatario_line.text()

        try:
            if numero_da_conta_do_destinatario != '':
                self.tela_transferir.nome_do_destinatario_line.setText(self.banco.contas[numero_da_conta_do_destinatario].titular.nome)
                self.tela_transferir.cpf_do_destinatario_line.setText(self.banco.contas[numero_da_conta_do_destinatario].titular.cpf[0:3] + '********')
            else:
                QMessageBox.information(None, "LEBANK", "Informe o numero da conta do destinatario")
        except:
            QMessageBox.information(None, "LEBANK", "Ocorreu um erro")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
