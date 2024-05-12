# Diffie-Hellman Key Exchange Startup Documentation

## Introduction
Welcome to the startup documentation for the Diffie-Hellman Key Exchange implementation in Python. This document provides step-by-step instructions to set up and run the provided code for securely exchanging cryptographic keys over a public channel using the Diffie-Hellman protocol.

## Prerequisites
Before proceeding, ensure that you have the following prerequisites installed:
- Python 3.x
- Required Python libraries: `socket`, `tkinter`

## Installation
1. **Clone the Repository**: Clone the repository containing the Diffie-Hellman Key Exchange implementation to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where you have cloned the repository.

## Setup
### Server Setup
1. **Navigate to Server Directory**: Navigate to the `Sockets` directory within the cloned repository.

2. **Start the Server**: Execute the `Server.py` script by running the following command:

```
python3 Server.py
```

   

This command will start the server, which will listen for incoming client connections on a specified port.

### Client Setup
1. **Navigate to Client Directory**: Navigate to the `Sockets` directory within the cloned repository.

2. **Start a Client Instance**: Execute the `Client.py` script by running the following command:

This command will start a client instance and initiate the Diffie-Hellman key exchange with the server.

3. **Input Secret Key**: When prompted, input a secret key. This key will be used in the Diffie-Hellman key exchange process.

4. **Initiate Key Exchange**: The client will initiate the key exchange process with the server, establishing a shared secret key securely.

## Usage
1. **Communication**: Once the key exchange is complete, the client and server can communicate securely using the shared secret key.

2. **Additional Functionality**: The client script also includes a graphical user interface (GUI) built using `tkinter`. You can interact with the GUI to input the secret key and display received messages.

## Conclusion
Congratulations! You have successfully set up and initiated the Diffie-Hellman Key Exchange implementation. You can now securely exchange cryptographic keys over a public channel using the provided Python code.



# Technical Documentation for Diffie-Hellman Key Exchange Implementation

## Overview
The provided code implements the Diffie-Hellman key exchange protocol using Python. Diffie-Hellman is a method for securely exchanging cryptographic keys over a public channel. This documentation aims to provide insights into the implementation, including key components, functionality, and usage instructions.

## Components

### 1. `DiffieHellman.py`
- **DH Class**: 
  - `__init__(self)`: Initializes the Diffie-Hellman parameters (`p` and `g`).
  - `calcPublicSecret(self, secret)`: Calculates the public key based on the private secret input.
  - `calcSharedSecret(self, privSecret, publicSecret)`: Computes the shared secret key between two parties using their private and received public keys.

### 2. `Client.py`
- **ClientSocket Class**:
  - `__init__(self, port)`: Initializes a client socket and Diffie-Hellman instance.
  - `receive(self)`: Receives messages from the server.
  - `create_header(self, message)`: Creates a header for sending messages.
  - `send(self, message)`: Sends messages to the server.
  - `initDiffieHellman(self)`: Initiates the Diffie-Hellman key exchange process.
  - `start_client(self)`: Starts the client and initiates the Diffie-Hellman key exchange.

### 3. `Server.py`
- **Server Class**:
  - `__init__(self, port)`: Initializes the server with a specified port.
  - `receive(self, client)`: Receives messages from clients.
  - `create_header(self, message)`: Creates a header for sending messages.
  - `write(self, message, client)`: Writes messages back to clients.
  - `initDiffieHellman(self, client)`: Initiates the Diffie-Hellman key exchange process for a client.
  - `handle_client(self, client)`: Handles client connections and initiates Diffie-Hellman key exchange.
  - `run_server(self)`: Starts the server and listens for client connections.

## Usage Instructions
1. **Server Setup**:
   - Execute `Server.py` to start the server. It will listen for incoming client connections on the specified port.

2. **Client Setup**:
   - Execute `Client.py` to start a client instance.
   - Input a secret key when prompted. This key will be used in the Diffie-Hellman key exchange.
   - The client will initiate the key exchange with the server.

3. **Key Exchange**:
   - The Diffie-Hellman key exchange will be performed between the client and server, allowing them to establish a shared secret key securely.

4. **Communication**:
   - Once the key exchange is complete, the client and server can communicate securely using the shared secret key.

## Additional Notes
- **Security**: While Diffie-Hellman provides a secure method for key exchange, it's crucial to implement additional security measures for data transmission, such as encryption.
- **Error Handling**: The code provides basic error handling for message transmission; however, further enhancements can be made to improve robustness.
- **Dependencies**: The code utilizes the `socket` library for network communication and `tkinter` for the client's graphical user interface. Ensure these libraries are installed to run the code successfully.

## Conclusion
This technical documentation provides an overview of the Diffie-Hellman key exchange implementation, including its components, functionality, and usage instructions. By following the provided guidelines, users can securely exchange cryptographic keys over a public channel using the provided Python code.
