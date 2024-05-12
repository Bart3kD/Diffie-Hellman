# Diffie-Hellman Protocol

### How it works

- The server starts and waits for 2 clients to connect
- After 2 clients connect the server sends information to te client that the key exchange has started
- The client inputs an integer key which cannot be bigger than the p (check DH class)
- On the client side the public key is calculated for each user
- The server receives both the public keys and calculates the shared public key
- If the shared key is the same for both clients then it gets sent to the users, if not, then an error pops up
- The clients receives the shared key

### How to start it

- Start the Server.py in the Sockets folder - it should open the command line and print "Server started"
- Start the Client.py in the Sockets folder - it should open the command line and a few seconds later a window with an input for your key

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
