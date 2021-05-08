class Pessoa:

		__slots__ = ['_nome', '_endereco', '_cpf', '_nascimento']

		def __init__(self, nome, endereco, cpf, nascimento):
			self._nome = nome
			self._endereco = endereco
			self._cpf = cpf
			self._nascimento = nascimento

		@property
		def nome(self):
			return self._nome

		@property
		def endereco(self):
			return self._endereco
		
		@property
		def cpf(self):
			return self._cpf
		
		@property
		def nascimento(self):
			return self._nascimento
		
		@nome.setter
		def nome(self, nome):
			self._nome = nome

		@endereco.setter
		def endereco(self, endereco):
			self._endereco = endereco

class Cadastro:

	__slots__ = ['_dicionario_pessoas']

	def __init__(self):
		self._dicionario_pessoas = {}

	@property
	def dicionario_pessoas(self):
		return self._dicionario_pessoas
	

	def cadastra(self, pessoa):
		try:
			if pessoa.cpf in self.dicionario_pessoas:
				return False
			else:
				self.dicionario_pessoas[pessoa.cpf] = pessoa
				return True
		except:
			return False

	def busca(self, cpf):
		try:
			return self.dicionario_pessoas[cpf]
		except:
			return None
