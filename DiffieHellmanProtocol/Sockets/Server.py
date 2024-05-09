from typing import Dict, Any
from DiffieHellmanProtocol.DiffieHellmann.DiffieHellman import DH
import socket
import threading
import time

class Server:
    """
    Represents a server for facilitating communication using the Diffie-Hellman key exchange protocol.
    """
    def __init__(self, port: int) -> None:
        """
        Initializes the Server object.

        Args:
            port (int): The port number for the server.
        """
        self.port: int = port
        self.clients: Dict[Any, Any] = {}
        self.clients_keys: Dict[Any, int] = {}
    
    def receive(self, client: socket.socket) -> str:
        """
        Receives a message from a client.

        Args:
            client (socket.socket): The client socket.

        Returns:
            str: The received message.
        """
        message_len: int = int(client.recv(5).decode("utf-8"))
        message: str = client.recv(message_len)

        if len(message) != message_len:
            self.write("Error while receiving the message", client)
        else:
            return message.decode("utf-8").strip("\n")

    def create_header(self, message: str) -> str:
        """
        Creates a header for a message.

        Args:
            message (str): The message.

        Returns:
            str: The header for the message.
        """
        header: str = f"{len(message):<5}"
        return header

    def write(self, message: str, client: socket.socket) -> None:
        """
        Writes a message to a client.

        Args:
            message (str): The message to be sent.
            client (socket.socket): The client socket.
        """
        message += '\n'
        header: str = self.create_header(message)

        client.send(header.encode('utf-8'))
        client.send(message.encode('utf-8'))
    
    def initDiffieHellman(self, client: socket.socket) -> None:
        """
        Initiates the Diffie-Hellman key exchange process with a client.

        Args:
            client (socket.socket): The client socket.
        """
        if self.receive(client) != "connected":
            print("Error while connecting")
        
        client_public_key: int = int(self.receive(client))
        
        self.clients_keys[client] = client_public_key                

        if len(self.clients_keys) == 2:
            for other_client in self.clients:
                for cl, k in self.clients_keys.items():
                    if other_client != cl:
                        self.write(str(k), other_client)
    
    def handle_client(self, client: socket.socket) -> None:
        """
        Handles communication with a client.

        Args:
            client (socket.socket): The client socket.
        """
        time.sleep(4)
        self.clients[client] = client
        self.initDiffieHellman(client)
    
    def run_server(self) -> None:
        """Runs the server."""
        print("Server started")
        server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", self.port))
        server_socket.listen(10)

        while 1:
            client_socket, addr = server_socket.accept()
            client_handler: threading.Thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()


server = Server(5001)
server.run_server()
