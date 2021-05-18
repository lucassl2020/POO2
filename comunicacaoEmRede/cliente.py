from socket import socket, AF_INET, SOCK_STREAM

ip = 'localhost'
port = 8000
address = ((ip, port))

cliente_socket = socket(AF_INET, SOCK_STREAM)
cliente_socket.connect(address)

while(True):
	mensagem = input('Digite uma mensagem para enviar ao servidor: ')
	cliente_socket.send(mensagem.encode())
	print('Mensagem enviada')

	if mensagem == 'EXIT':
		cliente_socket.send(mensagem.encode())
		break

	resposta = cliente_socket.recv(1024).decode()

	print("Resposta: " + resposta)

cliente_socket.close()
