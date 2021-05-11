from socket import socket, AF_INET, SOCK_STREAM

ip = 'localhost'
port = 8000
address = ((ip, port))

cliente_socket = socket(AF_INET, SOCK_STREAM)
cliente_socket.connect(address)

print('Envie a mensagem EXIT para desconectar do servidor')
while(True):
	mensagem = input('Digite uma mensagem para enviar ao servidor: ')
	cliente_socket.send(mensagem.encode())
	print('Mensagem enviada')

	resposta = cliente_socket.recv(1024).decode()

	if resposta == 'EXIT':
		cliente_socket.send('EXIT'.encode())
		break
	else:
		print(resposta)

cliente_socket.close()
