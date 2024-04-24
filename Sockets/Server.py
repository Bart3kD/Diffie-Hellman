import socketserver
from DiffieHellmann import DiffieHellman
import json

class ServerSocket(socketserver.BaseRequestHandler):
    def __init__(self):
        self.__debugflag = self.server.conn
        self.__dh = DiffieHellman.DH()

    def initDiffieHellman(self):
        if self.request.recv(1024).decode() != "connected":
            print("Error while connecting")
        
        publicSecret = self.__dh.calcPublicSecret()

        step1 = {
            "dh-keyexchange": {
            "step": 1,
            "base": self.__dh.base,
            "prime": self.__dh.sharedPrime,
            "publicSecret": publicSecret
            }
        }

        step1_str = str(step1)
        self.request.send(step1_str.encode())


        step2 = self.request.recv(1024)

        if self.__debugflag:
            print(step2)

        jsonData = json.loads(step2.decode())
        jsonData = jsonData["dh-keyexchange"]

        publicSecret = int(jsonData["publicSecret"])

        self.__dh.calc_shared_secret(publicSecret)
    
    def handle(self):
        print("[{}] Client connected.".format(self.client_address[0]))

        self.initDiffieHellman()
        print("> The secret key is {}\n".format(self.__dh.key))

def start_server(debugflag):
    server = socketserver.ThreadingTCPServer(("", 50000), ServerSocket)

    server.conn = debugflag

    server.serve_forever()