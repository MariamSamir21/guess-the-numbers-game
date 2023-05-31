#These lines import the necessary modules: socket for network communication and tkinter for creating the GUI.
import socket
import tkinter as tk

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

# These lines create the main window for the GUI using the Tk() constructor from tkinter
#They set the window title to "Guess the Number" and the dimensions to 300 pixels width and 200 pixels height.
window = tk.Tk()
window.title("Guess the Number")
window.geometry("300x200")

# This line creates a label widget using tk.Label() and assigns it to the instructions_label  variable
#It sets the text of the label to the welcome message and packs it into the window.
instructions_label = tk.Label(window, text="Welcome to Guess the Number!\nI'm thinking of a number between 1 and 50.")
instructions_label.pack()

# This line creates an entry widget using tk.Entry() and assigns it to the guess_entry variable
# It creates an input field where the player can enter their guess and packs it into the window.
guess_entry = tk.Entry(window)
guess_entry.pack()

# This line creates a label widget using tk.Label() and assigns it to the response_label variable
#It will display the server's response, so it is initially empty, and it is packed into the window.
response_label = tk.Label(window)
response_label.pack()

# These lines define the send_guess() function
# It retrieves the player's guess from the guess_entry widget, sends it to the server using the client socket
#receives the server's response, updates the response_label widget, and checks if the game is over
# If it is, it disables the guess entry field and the send button
def send_guess():
    guess = guess_entry.get()

    # Send the guess to the server
    client_socket.sendall(guess.encode())

    # Receive and update the server's response
    response = client_socket.recv(1024).decode()
    response_label.config(text=response)

    # Check if the game is over
    if "Congratulations" in response or "Game over" in response:
        guess_entry.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)

# This line creates a button widget using tk.Button() and assigns it to the send_button variable
# It displays the text "Send Guess" on the button and associates the send_guess() function as the command to execute when the button is clicked
send_button = tk.Button(window, text="Send Guess", command=send_guess)
send_button.pack()

# This line starts the GUI main loop, which listens for events and updates the GUI accordingly
window.mainloop()

# Close the client socket terminating the connection between the client and the server
client_socket.close()
