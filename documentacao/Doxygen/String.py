'''
Módulo responsável por manipular strings
'''

class String():
	"""Classe responsavel por armazenar uma string e definir operações com ela

	Atributos:
		self._string: 
			Descrição: String en que serão feitas as operações
			Tipo: str
	"""
	def __init__(self, string):
		self._string = string

	@property
	def string(self):
		return self._string
	
	@string.setter
	def string(self, string):
		self._string = string

	def concatenar(self, texto):
		"""Une um texto a string separados por um espaço.

		Parâmetros:
			texto: 
				Descrição: Texto que será unido a string
				Tipo: str
		"""
		self.string += " " + texto

	def tamanho(self):
		"""Calcula e retorna o tamanho da string que o objeto armazena
		
		Retorno: 
			Descrição: Tamanho da string que o objeto armazena
			Tipo: int
		"""
		return len(self.string)
