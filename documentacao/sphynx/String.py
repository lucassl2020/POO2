'''
Classe responsavel por armazenar uma string e definir operações com ela

    :ivar self._string: String armazenada pelo objeto
    :vartype self._string: str

 '''

class String():
	def __init__(self, string):
		self._string = string

	@property
	def string(self):
		return self._string
	
	@string.setter
	def string(self, string):
		self._string = string

	def concatenar(self, texto):
		"""
		Une um texto a string separados por um espaço.

		:param texto: Texto que será unido a string
		:type request_name: str
		"""
		self.string += " " + texto

	def tamanho(self):
		"""
		Calcula e retorna o tamanho da string que o objeto armazena
		
		:return: Tamanho da string que o objeto armazena
		"""
		return len(self.string)

if __name__ == "__main__":
	s = String("Lucas")

	print(s.string)

	print(s.tamanho())

	s.string = "Silva Lopes"

	print(s.string)

	print(s.tamanho())
