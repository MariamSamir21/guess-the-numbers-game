import socket
#This line imports the socket module, which provides a low-level interface for network communication.

# This line creates a socket object client_socket using the socket.socket() constructor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#This line establishes a connection to the server at the address "localhost"  and port 12345 using the connect() method of the client socket
client_socket.connect(("localhost", 12345))

# Receive initial instructions from the server
#It uses the recv() method of the client socket to receive data from the server
#The received data is decoded from bytes to a string using the decode() method, and then printed to the console.
print(client_socket.recv(1024).decode())

# Game loop
while True:
    # Get the player's guess
    guess = input("Enter your guess: ")

    # This line sends the player's guess to the server. It uses the sendall() method of the client socket to send the data
    #The guess is encoded into bytes using the encode() method before being sent.
    client_socket.sendall(guess.encode())

    # Receive and print the server's response
    response = client_socket.recv(1024).decode()
    print(response)

    # Check if the game is over
    if "Congratulations" in response or "Game over" in response:
        break

# Close the client socket
client_socket.close()
