from Conta import Conta
from Cliente import Cliente

class Banco():

	def __init__(self):
		self._clientes = {}
		self._contas = {}
		self._conta_atual = None

	@property
	def clientes(self):
		return self._clientes

	@property
	def contas(self):
		return self._contas

	@property
	def conta_atual(self):
		return self._conta_atual

	@conta_atual.setter
	def conta_atual(self, valor):
		self._conta_atual = valor
	
	def clienteCadastrar(self, cliente):
		try:
			self.clientes[cliente.cpf] = cliente
			return True
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
