import socket
from DiffieHellmanProtocol.DiffieHellmann import DiffieHellman

class ClientSocket:
    def __init__(self, port):
        self.__dh = DiffieHellman.DH()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port

    def receive(self):
        message_len = int(self.sock.recv(5).decode("utf-8"))
        message = self.sock.recv(message_len).decode('utf-8')

        if len(message) != message_len:
            print("Error while receiving message")

        return message

    def create_header(self, message):
        header = f"{len(message):<5}"
        return header

    def send(self, message):
        header = self.create_header(message)

        self.sock.send(header.encode('utf-8'))
        self.sock.send(message.encode('utf-8'))
        
    def initDiffieHellman(self):

        self.send("connected")
        print("connected")

        secret = int(input("Input your secret key: "))
        calcedPubSecret = str(self.__dh.calcPublicSecret(secret))
        self.send(calcedPubSecret)

        bob_key = int(self.receive())

        sharedSecret = self.__dh.calcSharedSecret(secret, bob_key)
        self.send(str(sharedSecret))      
        print("Your shared key is: ", sharedSecret)  

    def start_client(self):
        try:
            self.sock.connect(("localhost", self.port));

            self.initDiffieHellman()
        finally:
            self.sock.close()

client = ClientSocket(5000)
client.start_client()

