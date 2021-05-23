from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from Conta import Conta
from Cliente import Cliente


class Banco():
	def __init__(self):
		self._clientes = {}
		self._contas = {}
		self.requests = {}
		self.create_requests()
		self.create_server()
		self.start_server()

	@property
	def clientes(self):
		return self._clientes

	@property
	def contas(self):
		return self._contas

	def create_server(self):
		self.host = 'localhost'
		self.port = 8000
		self.address = (self.host, self.port)

		self.server_socket = socket(AF_INET, SOCK_STREAM)
		self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.server_socket.bind(self.address)
		self.server_socket.listen(10)

	def adicionar_request(self, request_name, request_func):
		self.requests[request_name] = request_func

	def create_requests(self):
		self.adicionar_request("cadastrar_cliente", self.cadastrarCliente)
		self.adicionar_request("login", self.login)
		self.adicionar_request("get_titular", self.getTitular)
		self.adicionar_request("get_saldo", self.getSaldo)
		self.adicionar_request("get_limite", self.getLimite)
		self.adicionar_request("get_historico", self.getHistorico)
		self.adicionar_request("get_titular_cpf_destinatario", self.getTitularCpfDestinatario)
		self.adicionar_request("sacar", self.sacar)
		self.adicionar_request("depositar", self.depositar)
		self.adicionar_request("transferir", self.transferir)

	def requestReceber(self):
		request = self.con.recv(1024).decode()

		request_list = request.split(",")

		return request_list[0], request_list[1:]

	def start_server(self):
		print("START SERVER...")

		self.con, self.cliente = self.server_socket.accept()

		while(True):
			request_name, request_parameters = self.requestReceber()
			
			try:
				func = self.requests[request_name]
				
				resposta = func(request_parameters)
			except:
				break

			self.con.send(resposta.encode())

		self.server_socket.close()

	def cadastrarCliente(self, request_parameters):
		print("Cadastrando cliente")

		resposta = 'False'

		cliente = Cliente(request_parameters[0], request_parameters[1], request_parameters[2])

		if cliente.cpf not in self.clientes and cliente.cpf.isdigit() and len(cliente.cpf) == 11:
			self.clientes[cliente.cpf] = cliente
							
			if self.cadastrarConta(Conta(cliente, request_parameters[3])):
				resposta = "True"
				resposta += ","
				resposta += str(Conta.qtd_de_contas())

		return resposta

	def cadastrarConta(self, conta):
		print("Cadastrando conta")

		self.contas[conta.numero] = conta
		return True

	def login(self, request_parameters):
		print("Verificando login")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"

		return resposta

	def getTitular(self, request_parameters):
		print("Buscando e retornando titular")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ','
			resposta += self.contas[request_parameters[0]].titular.nome
			resposta += ' '
			resposta += self.contas[request_parameters[0]].titular.sobrenome

		return resposta

	def getSaldo(self, request_parameters):
		print("Buscando e retornando saldo")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ','
			resposta += str(self.contas[request_parameters[0]].saldo)

		return resposta

	def getLimite(self, request_parameters):
		print("Buscando e retornando limite")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = 'True'
			resposta += ','
			resposta += str(self.contas[request_parameters[0]].limite)

		return resposta

	def getHistorico(self, request_parameters):
		print("Buscando e retornando historico")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = "True"
			resposta += ","
			resposta += self.contas[request_parameters[0]].extrato()

		return resposta

	def getTitularCpfDestinatario(self, request_parameters):
		print("Buscando e retornando titular e cpf do destinatario")

		resposta = "False"

		try:
			if self.contas[request_parameters[0]].senha == request_parameters[1]:
				resposta = "True"
				resposta += ","
				resposta += self.contas[request_parameters[2]].titular.nome
				resposta += ' '
				resposta += self.contas[request_parameters[2]].titular.sobrenome
				resposta += ','
				resposta += self.contas[request_parameters[2]].titular.cpf[0:3]
		except:
			pass

		return resposta

	def sacar(self, request_parameters):
		print("Realizando saque")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = str(self.contas[request_parameters[0]].saca(float(request_parameters[2])))

		return resposta

	def depositar(self, request_parameters):
		print("Realizando deposito")

		resposta = "False"

		if self.contas[request_parameters[0]].senha == request_parameters[1]:
			resposta = str(self.contas[request_parameters[0]].deposita(float(request_parameters[2])))

		return resposta

	def transferir(self, request_parameters):
		print("Realizando transferencia")

		resposta = "False"
		try:
			if self.contas[request_parameters[0]].senha == request_parameters[1]:
				resposta = str(self.contas[request_parameters[0]].transfere(self.contas[request_parameters[2]], float(request_parameters[3])))
		except:
			pass

		return resposta


if __name__ == "__main__":
	banco = Banco()
