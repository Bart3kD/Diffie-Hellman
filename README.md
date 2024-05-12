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

### Libraries I used
1. Typing
  - Union
  - Any
  - Dict
2. Socket
3. tkinter
4. customtkinter
5. threading
6. time

### DiffieHellman.py
This is where the calculations are made.

Functions:
##### - getValues:
Returns the prime modulus (p) and base (g) used in the Diffie-Hellman protocol. The function was made for testing purposes.
