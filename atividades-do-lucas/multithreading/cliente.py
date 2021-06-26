import socket

ip = "localhost"
port = 7003
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    mensagem = input("digite uma mensagem para enviar ao servidor: ")

    client_socket.send(mensagem.encode())

    print("mensagem recebida " + client_socket.recv(1024).decode())
    
    if mensagem == "bye":
        break

client_socket.close()