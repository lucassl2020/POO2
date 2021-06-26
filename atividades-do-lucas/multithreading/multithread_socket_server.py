import socket
import threading


class ClientThread(threading.Thread):

    _contador = 0

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.id = ClientThread._contador

        ClientThread._contador += 1

        print("Nova conexao: ", clientAddress)

    def run(self):
        print("Conectado de: ", clientAddress)

        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())

            print("from client{}: ".format(self.id), msg)

            if msg == "bye":
                break

        print("Client at ", clientAddress, " disconnected...")


if __name__ == "__main__":
    localhost = ""
    port = 7003
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((localhost, port))

    print("Servidor iniciado!")
    print("Aguardando nova conexão..")

    server.listen(1)
    while True:
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
