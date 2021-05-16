from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from Conta import Conta
from Cliente import Cliente


class Banco():
	def __init__(self):
		self._clientes = {}
		self._contas = {}
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

	def start_server(self):
		print("START SERVER...")

		self.con, self.cliente = self.server_socket.accept()

		while(True):
			self.recebe = self.requestReceber()

			print("RUNNING SERVER...")

			resposta = "False"

			if self.recebe[0] == "cadastrar_cliente":
				cliente = Cliente(self.recebe[1], self.recebe[2], self.recebe[3])
				if self.clienteCadastrar(cliente):
					if self.contaCadastrar(Conta(cliente, self.recebe[4])):
						resposta = "True"
						resposta += ","
						resposta += str(Conta.qtd_de_contas())

			elif self.recebe[0] == "login":
				resposta = str(self.login(self.recebe[1], self.recebe[2]))

			elif self.recebe[0] == "get_titular":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = "True"
					resposta += ','
					resposta += self.contas[self.recebe[1]].titular.nome
					resposta += ' '
					resposta += self.contas[self.recebe[1]].titular.sobrenome			

			elif self.recebe[0] == "get_saldo":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = "True"
					resposta += ','
					resposta += str(self.contas[self.recebe[1]].saldo)
			
			elif self.recebe[0] == "get_limite":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = 'True'
					resposta += ','
					resposta += str(self.contas[self.recebe[1]].limite)
			
			elif self.recebe[0] == "get_titular_cpf_destinatario":
				try:
					if self.contas[self.recebe[1]].senha == self.recebe[2]:
						resposta = "True"
						resposta += ","
						resposta += self.contas[self.recebe[3]].titular.nome
						resposta += ' '
						resposta += self.contas[self.recebe[3]].titular.sobrenome
						resposta += ','
						resposta += self.contas[self.recebe[3]].titular.cpf[0:3]
				except:
					pass

			elif self.recebe[0] == "sacar":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = str(self.contas[self.recebe[1]].saca(float(self.recebe[3])))

			elif self.recebe[0] == "depositar":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = str(self.contas[self.recebe[1]].deposita(float(self.recebe[3])))

			elif self.recebe[0] == "transferir":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = str(self.contas[self.recebe[1]].transfere(self.contas[self.recebe[3]], float(self.recebe[4])))
			
			elif self.recebe[0] == "get_historico":
				if self.contas[self.recebe[1]].senha == self.recebe[2]:
					resposta = "True"
					resposta += ","
					resposta += self.contas[self.recebe[1]].extrato()

			self.con.send(resposta.encode())

		self.server_socket.close()

	def requestReceber(self):
		request = self.con.recv(1024).decode()

		return request.split()

	def clienteCadastrar(self, cliente):
		try:
			if cliente.cpf not in self.clientes and cliente.cpf.isdigit() and len(cliente.cpf) == 11:
				self.clientes[cliente.cpf] = cliente
				return True
			return False
		except:
			return False 

	def contaCadastrar(self, conta):
		try:
			self.contas[conta.numero] = conta
			return True
		except:
			return False 

	def login(self, numero_da_conta, senha):
		try:
			if self.contas[numero_da_conta].senha == senha:
				return True
			return False
		except:
			return False


if __name__ == "__main__":
	banco = Banco()
