import socket 
#imports the socket module, which provides a low-level interface for network communication.

# Function to handle the game logic
def play_game(conn):
    # Set the range and generate the target number
    lower_bound = 1
    upper_bound = 50
    target_number = 30
    # initialize variables to keep track of the number of attempts made by the players and the maximum number of attempts allowed.
    attempts = 0
    max_attempts = 10

    # sends an initial welcome message to the client via the provided conn object. The message is sent as bytes using the sendall() method.
    conn.sendall(b"Welcome to Guess the Number!\nI'm thinking of a number between 1 and 50.\n")

    # Game loop
    while attempts < max_attempts:
        # This line receives the client's guess from the connection object conn. it uses recv  to receive the data
        # decode to convert the received bytes to a string
        #strip to remove any leading or trailing whitespace. The guess is then converted to an integer.
        guess = int(conn.recv(1024).decode().strip())
        print("Received guess:", guess)

        # increments the number of attempts made by the player.
        attempts += 1

        if guess == target_number:
            conn.sendall(b"Congratulations! You guessed the correct number.\n")
            break
        elif guess < target_number:
            conn.sendall(b"Higher!\n")
        else:
            conn.sendall(b"Lower!\n")

    # If the player runs out of attempts
    if attempts == max_attempts:
        conn.sendall(b"Game over! You did not guess the number within the allotted attempts.\n")

    # Close the connection
    conn.close()

# Set up the server socket
#This line creates a socket object server_socket using the socket.socket() constructor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#This line binds the server socket to the address "localhost" and port 12345. This is the address where the clients will connect to.
server_socket.bind(("localhost", 12345))
#This line starts listening for incoming connections on the server socket. The argument 2 specifies the maximum number of queued connections.
server_socket.listen(2)
print("Waiting for connections...")

# Accept two client connections
player1_conn, player1_addr = server_socket.accept()
print("Player 1 connected:", player1_addr)

player2_conn, player2_addr = server_socket.accept()
print("Player 2 connected:", player2_addr)

# Start the game for each player
play_game(player1_conn)
play_game(player2_conn)

# Close the server socket
server_socket.close()
