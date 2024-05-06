import socket
import time
from tkinter import *
import customtkinter

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
        

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()

        root.title('User client')
        root.geometry('600x350')

        connect_label = customtkinter.CTkLabel(root, text="connected", font=("Helvetica", 14))
        connect_label.pack(pady=10)

        my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
        my_label.pack(pady=40)

        my_entry = customtkinter.CTkEntry(root, 
                                        placeholder_text="Enter your key"

                                        )
        my_entry.pack(pady=20)

        def submit():
            secret = None

            while secret == None:
                try:
                    secret = int(my_entry.get())
                    print(secret)
                    print(help(self.__dh))
                    # print(self.__dh.getValues())
                except ValueError:
                    connect_label.configure(text="Please enter an integer key")
                calcedPubSecret = str(self.__dh.calcPublicSecret(secret))
                if calcedPubSecret == "False":
                    secret = None
                    connect_label.configure(text="Your key is too big, try again")
                else:
                    print(secret)
                    self.send(calcedPubSecret)
                    print(calcedPubSecret)
            
            bob_key = int(self.receive())

            sharedSecret = self.__dh.calcSharedSecret(secret, bob_key)
            self.send(str(sharedSecret))      
            my_label.configure(text="Your shared key is: " + str(sharedSecret))  

        my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
        my_button.pack(pady=10)

        root.mainloop()

    def start_client(self):
        try:
            self.sock.connect(("localhost", self.port));

            self.initDiffieHellman()
        finally:
            self.sock.close()

client = ClientSocket(5001)
client.start_client()

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# root = customtkinter.CTk()

# root.title('User client')
# root.geometry('600x350')

# connect_label = customtkinter.CTkLabel(root, text="connected", font=("Helvetica", 14))
# connect_label.pack(pady=10)

# my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
# my_label.pack(pady=40)

# my_entry = customtkinter.CTkEntry(root, 
#                                 placeholder_text="Enter your key"

#                                 )
# my_entry.pack(pady=20)

# def submit():
#     global value
#     value =  my_entry.get()

# my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
# my_button.pack(pady=10)



# root.mainloop()