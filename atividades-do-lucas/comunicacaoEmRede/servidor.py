from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

host = 'localhost'
port = 8000
address = (host, port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(address)
server_socket.listen(10)


while True:
	res = input('Sair ou continuar (s ou c)')
	if res == "s":
		break

	print('Aguardando conexao')
	con, cliente = server_socket.accept()

	print('\nConectado')
	print('Aguardando mensagem\n')

	while True:
		recebe = con.recv(1024).decode()
		print('Mensagem recebida: ' + recebe)

		if recebe == 'EXIT':
			break
		
		enviar = input('Digite uma mensagem para enviar ao cliente: ')
			
		con.send(enviar.encode())

server_socket.close()
