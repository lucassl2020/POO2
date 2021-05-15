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
			self.recebe = self.con.recv(1024).decode()
			self.recebe = self.recebe.split()
			print("RUNNING SERVER...")

			resposta = "False"
			
			if self.recebe[0] == "cadastrar_cliente":
				cliente = Cliente(self.recebe[1], self.recebe[2], self.recebe[3])
				if self.clienteCadastrar(cliente):
					if self.contaCadastrar(Conta(cliente, self.recebe[4])):
						resposta = "True" + ' ' + str(Conta.qtd_de_contas())
				self.con.send(resposta.encode())
			elif self.recebe[0] == "login":
				if self.login(self.recebe[1], self.recebe[2]):
					resposta = "True"

				self.con.send(resposta.encode())
			elif self.recebe[0] == "get_titular":
				if self.contas[self.recebe[2]].senha == self.recebe[2]:
					resposta = self.contas[self.recebe[1]].titular.nome
					resposta += ' '
					resposta += self.contas[self.recebe[1]].titular.sobrenome			

				self.con.send(resposta.encode())
			elif self.recebe[0] == "get_saldo":
				if self.contas[self.recebe[2]].senha == self.recebe[2]:
					resposta = str(self.contas[self.recebe[1]].saldo)

				self.con.send(resposta.encode())
			else:	
				self.con.send("".encode())

		self.server_socket.close()

	def clienteCadastrar(self, cliente):
		try:
			if cliente.cpf not in self.clientes:
				self.clientes[cliente.cpf] = cliente
				return True
			else:
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
				self.conta_atual = self.contas[numero_da_conta]
				return True
			return False
		except:
			return False

if __name__ == "__main__":
	banco = Banco()
