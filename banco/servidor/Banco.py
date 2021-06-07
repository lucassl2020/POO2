from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from Conta import Conta
from Cliente import Cliente
import mysql.connector as mysql


class Banco:
	"""

	O objeto Banco contém os metódos necessários para o processamento e armazenamento das informações requisitadas.
	
	:ivar self._clientes: Usado para armazenar os clientes em um dicionario onde a key é seu CPF
	:vartype self._clientes: dict
	:ivar self._contas: Usado para armazenar as contas em um dicionario onde a key é o numero da conta
	:vartype self._contas: dict
	:ivar self.requests: Usado para armazenar os requests em um dicionario onde a key é o request
	:vartype self.requests: dict

	"""
	def __init__(self):
		self.requests = {}

		self.create_requests()
		self.create_server()
		self.create_bd()
		self.start_server()

	def create_server(self):
		self.host = 'localhost'
		self.port = 8000
		self.address = (self.host, self.port)

		self.server_socket = socket(AF_INET, SOCK_STREAM)
		self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.server_socket.bind(self.address)
		self.server_socket.listen(10)

	def adicionar_request(self, request_name, request_func):
		"""

		Adiciona ao dicionario de request o nome e a função do respectivo request(instrução).

		:param request_name: Nome do request
		:type request_name: str
		:param request_func: Função do request
		:type request_func: func

		"""
		self.requests[request_name] = request_func

	def create_requests(self):
		self.adicionar_request("cadastrar_cliente", self.cadastrarCliente)
		self.adicionar_request("login", self.respostaAoLogin)
		self.adicionar_request("get_titular", self.getTitular)
		self.adicionar_request("get_saldo", self.getSaldo)
		self.adicionar_request("get_limite", self.getLimite)
		self.adicionar_request("get_historico", self.getHistorico)
		self.adicionar_request("get_titular_cpf_destinatario", self.getTitularCpfDestinatario)
		self.adicionar_request("sacar", self.sacar)
		self.adicionar_request("depositar", self.depositar)
		self.adicionar_request("transferir", self.transferir)

	def requestReceber(self):
		"""

		Recebe o request enviado pelo cliente decodifica ele, e depois transforma em lista
		sendo o separador a ",".

		:ivar request: Mensagem decodificada
		:vartype request: str
		:ivar request_list: Mensagem em formato de lista
		:vartype request_list: list

		:return: O primeiro indice(o nome da função do request) e seus parametros necessarios para a realização da mesmo)

		"""
		request = self.con.recv(1024).decode()

		request_list = request.split(",")

		return request_list[0], request_list[1:]

	def start_server(self):
		"""
		
		Inicia o servidor, aguarda a conexão, e responde os requests.

		:ivar request_name: Recebe o nome do request
		:vartype request_name: str
		:ivar request_parameters: Recebe os parametros necessário para o determinado request
		:vartype request_parameters: list
		:ivar func: Recebe a função do request
		:vartype resposta: Recebe a resposta da função requisitada
		:return: A resposta

		"""
		print("START SERVER...")

		self.con, self.cliente = self.server_socket.accept()

		while(True):
			request_name, request_parameters = self.requestReceber()
			
			func = self.requests[request_name]

			resposta = func(request_parameters)

			self.con.send(resposta.encode())

		self.server_socket.close()
	
	def applySqlCommand(self, sql_command, retorno=None):
		conexao = mysql.connect(host="localhost", db="lebankDB", user="root", passwd="")

		cursor = conexao.cursor()

		cursor.execute(sql_command)

		if retorno == "fetchall":
			valor_return = cursor.fetchall()
		elif retorno == "lastrowid":
			valor_return = cursor.lastrowid 
		else:
			valor_return = None

		conexao.commit()

		conexao.close()

		return valor_return

	def create_bd(self):
		self.applySqlCommand("SET default_storage_engine=InnoDB;")

		sql_command = """CREATE TABLE IF NOT EXISTS Clientes(
					id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
					nome TEXT NOT NULL, 
					sobrenome TEXT NOT NULL,
					cpf VARCHAR(11) NOT NULL UNIQUE
				);"""
		self.applySqlCommand(sql_command)

		sql_command = """CREATE TABLE IF NOT EXISTS Contas(
					numero INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
					saldo FLOAT NOT NULL,
					limite FLOAT NOT NULL,
					senha VARCHAR(32) NOT NULL,
					id_cliente INTEGER NOT NULL,
					CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES Clientes (id)
				);"""
		self.applySqlCommand(sql_command)

		sql_command = """CREATE TABLE IF NOT EXISTS Historicos(
					id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
					operacao TEXT NOT NULL, 
					id_conta INTEGER NOT NULL,
					CONSTRAINT fk_conta FOREIGN KEY (id_conta) REFERENCES Contas (numero)
				);"""
		self.applySqlCommand(sql_command)

	def cpfJaCadastrado(self, cpf):
		listaCpfsEncontrados = self.applySqlCommand("SELECT * from Clientes WHERE cpf= '%s'" % (cpf), retorno="fetchall")

		if listaCpfsEncontrados:
			return True

		return False

	def cadastrarCliente(self, request_parameters):
		"""

		Cria o cliente mas so o adiciona na lista de clientes quando é verificado a existencia de seu
		CPF na lista, se seu cpf é numerico e se tem 11 digitos. Apos isso conta do cliente é cadastrada juntamente
		com a senha colocada.Por fim retorna True se deu certo juntamente com a quantidade de contas criadas. 
		
		"""
		print("Cadastrando cliente")

		resposta = 'False'

		nome = request_parameters[0]
		sobrenome = request_parameters[1]
		cpf = request_parameters[2]
		senha = request_parameters[3]

		if (not self.cpfJaCadastrado(cpf)) and cpf.isdigit() and len(cpf) == 11:
			id_cliente = self.applySqlCommand("INSERT INTO Clientes (nome, sobrenome, cpf) VALUES ('%s','%s','%s')" % (nome, sobrenome, cpf), retorno="lastrowid")

			id_conta = self.applySqlCommand("INSERT INTO Contas (saldo, limite, senha, id_cliente) VALUES (%s,%s,MD5('%s'),%s)" % (0.00, 1000.00, senha, id_cliente), retorno="lastrowid")

			resposta = "True"
			resposta += ","
			resposta += str(id_conta)

			print("Cliente cadastrado\n")

		return resposta

	def login(self, numero_da_conta, senha):
		listaContasEncontradas = self.applySqlCommand("SELECT 1 from Contas WHERE numero= %s AND senha= MD5('%s')" % (numero_da_conta, senha), retorno="fetchall")

		if listaContasEncontradas:
			return True
		
		return False

	def respostaAoLogin(self, request_parameters):
		"""

		Verifica o login da conta por meio da sua senha cadastrada.
		
		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:type request_parameters: list
		:return: Retorna True se a senha coincidir e False se não.
		:rtype: str

		"""
		print("Verificando login")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]

		if self.login(numero_da_conta, senha):
			print("Logado com sucesso\n")

			resposta = "True"
		else:
			print("Falha no login\n")

		return resposta

	def getTitular(self, request_parameters):
		"""

		Retorna o nome e o sobrenome do titular da conta por meio do numero da conta.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando titular de uma conta")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT id_cliente from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			id_cliente = conta_logada[0]

			listaClientesEncontrados = self.applySqlCommand("SELECT nome, sobrenome from Clientes WHERE id= %s" % (id_cliente), retorno="fetchall")

			cliente_logado = listaClientesEncontrados[0]

			nome = cliente_logado[0]
			sobrenome = cliente_logado[1]

			resposta = "True"
			resposta += ','
			resposta += nome
			resposta += ' '
			resposta += sobrenome

			print("Titular encontrado\n")

		return resposta

	def getSaldo(self, request_parameters):
		"""

		Retorna o saldo da conta por meio do numero.
		
		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando saldo de uma conta")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT saldo from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			saldo = conta_logada[0]

			resposta = "True"
			resposta += ','
			resposta += str(saldo)

			print("Saldo encontrado\n")

		return resposta

	def getLimite(self, request_parameters):
		"""

		Retorna o limite da conta por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str

		"""
		print("Buscando limite de uma conta")

		resposta = "False"

		numero_da_conta = request_parameters[0]
		senha = request_parameters[1]

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT limite from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			limite = conta_logada[0]

			resposta = 'True'
			resposta += ','
			resposta += str(limite)

			print("Limite encontrado\n")

		return resposta

	def getHistorico(self, request_parameters):
		"""

		Retorna o historico da conta por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta e o segundo a senha.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str
		
		"""
		print("Buscando e retornando historico")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT numero from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			id_conta = conta_logada[0]

			listaHistoricosEncontrados = self.applySqlCommand("SELECT operacao from Historicos WHERE id_conta= %s" % (id_conta), retorno="fetchall")

			resposta = "True"
			resposta += ","

			for historico in listaHistoricosEncontrados:
				operacao = historico[0]

				resposta += operacao

		return resposta

	def getTitularCpfDestinatario(self, request_parameters):
		"""

		Retorna o nome, sobrenome e cpf da conta do destinatário por meio do numero.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta,o segundo a senha, o terceiro o numero da conta do destinatário.
		:return: Se der tudo certo True é retornado, juntamente com as informações requisitadas, divididas por virgula.
		:rtype: str
		
		"""
		print("Buscando titular e cpf do destinatario")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]
		numero_conta_destinatario = int(request_parameters[2])

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT id_cliente from Contas WHERE numero= %s" % (numero_conta_destinatario), retorno="fetchall")

			if listaContasEncontradas:
				conta_logada = listaContasEncontradas[0]
				id_cliente = conta_logada[0]

				listaClientesEncontrados = self.applySqlCommand("SELECT nome, sobrenome, cpf from Clientes WHERE id= %s" % (id_cliente), retorno="fetchall")

				if listaClientesEncontrados:
					cliente_destinatario = listaClientesEncontrados[0]
					nome = cliente_destinatario[0]
					sobrenome =  cliente_destinatario[1]
					cpf = cliente_destinatario[2]

					resposta = "True"
					resposta += ","
					resposta += nome
					resposta += ' '
					resposta += sobrenome
					resposta += ','
					resposta += cpf[0:3]

					print("Titular e cpf do destinatario encotrado\n")

		return resposta

	def sacar(self, request_parameters):
		"""

		Realiza o saque da conta por meio do metodo saca da classe Conta, passando o valor a ser retirado.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, o terceiro o valor a ser sacado.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""

		print("Realizando saque")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]
		valor_a_ser_sacado = float(request_parameters[2])

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT numero, saldo from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			id_conta = conta_logada[0]
			saldo = conta_logada[1]

			
			if valor_a_ser_sacado > 0 and valor_a_ser_sacado <= saldo:
				saldo -= valor_a_ser_sacado

				self.applySqlCommand("UPDATE Contas SET saldo= %s WHERE numero= %s" % (saldo, id_conta))

				operacao = "Saque no valor de " + str(valor_a_ser_sacado) + " reais\n\n"
				self.applySqlCommand("INSERT INTO Historicos (operacao, id_conta) VALUES ('%s',%s)" % (operacao, id_conta))

				resposta = "True"

				print("Saque realizado com sucesso\n")
			else:
				print("Saque falhou\n")
		

		return resposta

	def depositar(self, request_parameters):
		"""

		Realiza o deposito na conta por meio do metodo deposita da classe Conta, passando o valor a ser depositado.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, o terceiro o valor a ser depositado.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""
		print("Realizando deposito")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]
		valor_a_ser_depositado = float(request_parameters[2])

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT numero, saldo, limite from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			id_conta = conta_logada[0]
			saldo = conta_logada[1]
			limite = conta_logada[2]
 
			if valor_a_ser_depositado > 0 and saldo + valor_a_ser_depositado <= limite:
				saldo += valor_a_ser_depositado

				self.applySqlCommand("UPDATE Contas SET saldo= %s WHERE numero= %s" % (saldo, id_conta))

				operacao = "deposito no valor de " + str(valor_a_ser_depositado) + " reais\n\n"
				self.applySqlCommand("INSERT INTO Historicos (operacao, id_conta) VALUES ('%s',%s)" % (operacao, id_conta))

				resposta = "True"

				print("deposito realizado com sucesso\n")
			else:
				print("deposito falhou\n")

		return resposta

	def transferir(self, request_parameters):
		"""

		Realiza a transferencia para a conta por meio do metodo transfere da classe Conta, passando o valor a ser transferido.

		:param request_parameters: Os parametros necessários para a realização, sendo o primeiro indice o numero da conta, o segundo a senha, sendo o terceiro e quarto, o numero da conta do destinatário e o valor a ser transferido.
		:return: Se der tudo certo True é retornado.
		:rtype: str
		
		"""

		print("Realizando transferencia")

		resposta = "False"

		numero_da_conta = int(request_parameters[0])
		senha = request_parameters[1]
		numero_conta_destinatario = int(request_parameters[2])
		valor_a_ser_transferido = float(request_parameters[3])

		if self.login(numero_da_conta, senha):
			listaContasEncontradas = self.applySqlCommand("SELECT numero, saldo, id_cliente from Contas WHERE numero= %s" % (numero_da_conta), retorno="fetchall")

			conta_logada = listaContasEncontradas[0]
			id_conta = conta_logada[0]
			saldo = conta_logada[1]
			id_cliente = conta_logada[2]

			listaContasEncontradasDestinatario = self.applySqlCommand("SELECT numero, saldo, limite, id_cliente from Contas WHERE numero= %s" % (numero_conta_destinatario), retorno="fetchall")

			if listaContasEncontradasDestinatario:
				conta_destinatario = listaContasEncontradasDestinatario[0]
				id_conta_destinatario = conta_destinatario[0]
				saldo_destinatario = conta_destinatario[1]
				limite_destinatario = conta_destinatario[2]
				id_cliente_destinatario = conta_destinatario[3]
				
				if id_conta != id_conta_destinatario:
					if valor_a_ser_transferido > 0 and valor_a_ser_transferido <= saldo:
						saldo -= valor_a_ser_transferido

						if saldo_destinatario + valor_a_ser_transferido <= limite_destinatario:
							saldo_destinatario += valor_a_ser_transferido 

							self.applySqlCommand("UPDATE Contas SET saldo= %s WHERE numero= %s" % (saldo, id_conta))
							self.applySqlCommand("UPDATE Contas SET saldo= %s WHERE numero= %s" % (saldo_destinatario, id_conta_destinatario))

							listaClientesEncontrados = self.applySqlCommand("SELECT nome, sobrenome from Clientes WHERE id= %s" % (id_cliente_destinatario), retorno="fetchall")
							cliente = listaClientesEncontrados[0]
							nome_completo = cliente[0] + " " + cliente[1]

							operacao = "Transferencia para " + nome_completo + " no valor de " + str(valor_a_ser_transferido) + " reais\n\n"
							self.applySqlCommand("INSERT INTO Historicos (operacao, id_conta) VALUES ('%s',%s)" % (operacao, id_conta))

							listaClientesEncontrados = self.applySqlCommand("SELECT nome, sobrenome from Clientes WHERE id= %s" % (id_cliente), retorno="fetchall")
							cliente = listaClientesEncontrados[0]
							nome_completo = cliente[0] + " " + cliente[1]

							operacao = "Transferencia recebida de " + nome_completo + " no valor de " + str(valor_a_ser_transferido) + " reais\n\n"
							self.applySqlCommand("INSERT INTO Historicos (operacao, id_conta) VALUES ('%s',%s)" % (operacao, id_conta_destinatario))

							resposta = "True"

							print("Transferencia realizada com sucesso\n")

		return resposta


if __name__ == "__main__":
	banco = Banco()
