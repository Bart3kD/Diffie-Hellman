import socket
from tkinter import *
import customtkinter
from typing import Union, Any

from DiffieHellmanProtocol.DiffieHellmann import DiffieHellman

"""
This is the file where the whole user functionality was made.
"""


class ClientSocket:
    """
    Represents a user's socket for communicating using the Diffie-Hellman key exchange protocol.
    """


    def __init__(self, port: int) -> None:
        """
        Initializes the ClientSocket object.

        Args:
            port (int): The port number for the client socket.
        """


        self.__dh = DiffieHellman.DH()
        self.sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port: int = port

    def receive(self) -> str:
        """
        Receives a message from the server.

        Returns:
            str: The received message.
        """


        message_len: int = int(self.sock.recv(5).decode("utf-8"))
        message: str = self.sock.recv(message_len).decode('utf-8')

        if len(message) != message_len:
            print("Error while receiving message")

        return message

    def create_header(self, message: str) -> str:
        """
        Creates a header for the message.

        Args:
            message (str): The message.

        Returns:
            str: The header for the message.
        """
        

        header: str = f"{len(message):<5}"
        return header

    def send(self, message: str) -> None:
        """
        Sends a message to the server.

        Args:
            message (str): The message to be sent.
        """


        header: str = self.create_header(message)

        self.sock.send(header.encode('utf-8'))
        self.sock.send(message.encode('utf-8'))
        
    def initDiffieHellman(self) -> None:
        """
        Initializes the Diffie-Hellman key exchange process with the server.
        """


        self.send("connected")

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root: Tk = customtkinter.CTk()

        root.title('User client')
        root.geometry('600x350')

        connect_label: Label = customtkinter.CTkLabel(root, text="connected", font=("Helvetica", 14))
        connect_label.pack(pady=10)

        my_label: Label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
        my_label.pack(pady=40)

        my_entry: Entry = customtkinter.CTkEntry(root, placeholder_text="Enter your key")
        my_entry.pack(pady=20)

        def validate_input(event: Any = None) -> None:
            """Validate the input value in the Entry widget."""
            current_value: str = my_entry.get()
            if current_value:
                try:
                    value = int(current_value)
                    if value > client._ClientSocket__dh.p:
                        connect_label.configure(text="Your key is too big, try again")
                    else:
                        connect_label.configure(text="")  
                except ValueError:
                    connect_label.configure(text="Please enter an integer key")

        my_entry.bind('<Key>', validate_input)

        def update_label(text: str) -> None:
            """Update the label text."""
            my_label.configure(text=text)
            root.update()  

        def submit() -> None:
            """
            Callback function for the submit button. Performs Diffie-Hellman key exchange with the server.
            """
            secret: Union[int, None] = None



            current_value: str = my_entry.get()
            if current_value:
                try:
                    value = int(current_value)
                    if value > client._ClientSocket__dh.p:
                        connect_label.configure(text="Your key is too big, try again")
                        return
                except ValueError:
                    connect_label.configure(text="Please enter an integer key")
                    return

            while secret is None:
                try:
                    secret = int(current_value)
                except ValueError:
                    connect_label.configure(text="Please enter an integer key")
                    return  

                calcedPubSecret: Union[str, bool] = str(client._ClientSocket__dh.calcPublicSecret(secret))
                if calcedPubSecret == "False":
                    connect_label.configure(text="Your key is too big, try again")
                    update_label("Your key is too big, try again")
                    secret = None  
                else:
                    client.send(calcedPubSecret)
            
            bob_key: int = int(client.receive())
            sharedSecret: int = client._ClientSocket__dh.calcSharedSecret(secret, bob_key)
            client.send(str(sharedSecret))
            my_label.configure(text="Your shared key is: " + str(sharedSecret))
            update_label("Your shared key is: " + str(sharedSecret))  




        my_button: Button = customtkinter.CTkButton(root, text="Submit", command=submit)
        my_button.pack(pady=10)

        root.mainloop()

    def start_client(self) -> None:
        """
        Starts the client socket and initiates the Diffie-Hellman key exchange process.
        """


        try:
            self.sock.connect(("localhost", self.port))
            self.initDiffieHellman()
        finally:
            self.sock.close()


client = ClientSocket(5001)
client.start_client()
