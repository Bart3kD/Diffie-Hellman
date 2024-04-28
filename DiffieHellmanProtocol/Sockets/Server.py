from DiffieHellmanProtocol.DiffieHellmann.DiffieHellman import DH
import socket
import threading
import time

class Server:
    def __init__(self,port):
        self.port = port
        self.clients = {}
        self.clients_keys = {}
    
    def receive(self, client):
        message_len = int(client.recv(5).decode("utf-8"))
        message = client.recv(message_len)

        if len(message) != message_len:
            self.write("Error while receiving the message", client)
        else:
            return message.decode("utf-8").strip("\n")

    def create_header(self, message):
        header = f"{len(message):<5}"
        return header

    def write(self, message, client):
        message += '\n'
        header = self.create_header(message)

        client.send(header.encode('utf-8'))
        client.send(message.encode('utf-8'))
    
    def initDiffieHellman(self, client):
        if self.receive(client) != "connected":
            print("Error while connecting")
        
        client_public_key = int(self.receive(client))
        
        self.clients_keys[client] = client_public_key                

        if len(self.clients_keys) == 2:
            for other_client in self.clients:
                for cl, k in self.clients_keys.items():
                    if other_client != cl:
                        self.write(str(k), other_client)
    
    def handle_client(self, client):
        time.sleep(4)
        self.clients[client] = client
        self.initDiffieHellman(client)
    
    def run_server(self):
        print("Server started")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", self.port))
        server_socket.listen(10)

        while 1:
            client_socket, addr = server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()


server = Server(5000)
server.run_server()
