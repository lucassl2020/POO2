from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

host = 'localhost'
port = 8000
address = (host, port)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(address)
server_socket.listen(10)

print('Aguardando conexao')



print('Conectado')
print('Aguardando mensagem')

while(True):
	recebe = con.recv(1024)
	print('Mensagem recebida: ' + recebe.decode())

	if recebe.decode() == 'EXIT':
		con.send('EXIT'.encode())
		break
	
	enviar = input('Digite uma mensagem para enviar ao cliente: ')
		
	con.send(True)

server_socket.close()
