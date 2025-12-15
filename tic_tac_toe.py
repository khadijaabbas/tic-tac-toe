'''
This code implements a game of tic-tac-toe, allowing the player to play 
against the computer. It checks for winning conditions, ties and ensures that
the game runs smoothly.

Overall, it provides a fun and efficent tic-tac-toe experience, demonstarting 
core python concepts.
'''




# Import random module to shuffle the computer's player position
import random

# Initalize the game board with empty spaces
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

# Set the current player to "X", initalize the winner and the game running
current_player = "X"
winner = None 
game_running = True 

# Function to print the current state of the board
def print_board(board):
    # Print the board in a 3x3 grid format
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    
# Function that handles the player's input     
def input_player(board):
    global current_player
    # Ask the user to enter a position
    input1 = int(input("Enter a number between 1 and 9: "))
    # Check if the input is valid and if the spot is avaliable
    if input1 >= 1 and input1 <= 9 and board[input1-1] == "-":
        # PLace the player's symbol onn the board
        board[input1-1] = current_player 
        # Switch the player
        current_player = "O" if current_player == "X" else "X" 
    else:
        # Print a message if the spot is already taken
        print("That spot is taken!") 
       
        
# Function to check for horizontal winning conditions on the board        
def horizontal(board):
    # Access the winner variable defined in the global scope
    global winner 
    # Check each row for a win
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner == board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner == board[6]
        return True
    
# Function to check for vertical winning conditions on the board        
def vertical(board): 
    # Access the winner variable defined in the global scope
    global winner 
    # Check each colum for a win
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 
 
# Function to check for diagonal winning conditions on the board            
def diagonal(board):
    # Access the winner variable defined in the global scope
    global winner
    # Check the diagonals for a win
    if board[0] == board[4] == board[8] and  board[0] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and  board[2] != "-":
        winner = board[2]
        return True 
   
# Function to check for a tie     
def check_tie(board):
    # Check if theres no empty spaces left on thr board
    if "-" not in board:
        # If theres no empty spaces left, print the current board and print that there is a tie 
        print_board(board)
        print("It's a tie!")
        # Return True to show the game is tied
        return True 

# Function to check if there is a winner        
def check_winner():
    # Check if there is a win condition by calling the horizontal, vertical and diagnoal functions
    if diagonal(board) or vertical(board) or horizontal(board):
        # check and print who the winner is 
        if winner == "X":
            print("X is the winner!")
        elif winner == "O":
            print("O is the winner!")
        # Return True to show there is a winner
        return True 
        
# Function for the computer's move        
def computer(board):
    # Access the current_player variable defined in the global scope
    global current_player
    while current_player == "O":
        # Choose a random postion between the range 0 to 8
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O" # Place the compurer's symbol on the board 
            current_player = "X" # Switch the player

# open output file in write mode        
output_file = open("output.txt", "r")        

# Display scores from the file
with output_file as file:
     print("\nWinner:")
     print(file.read())
    
        
# Main game loop
while game_running:
    print_board(board) # Print the current board
    input_player(board) # Take the player's input 
    if check_winner() or check_tie(board): # Check for a winner or a tie
        break
    computer(board) # Execute the computer's move
    if check_winner() or check_tie(board): # Check for a winner or a tie
        break

# # Close output file
# output_file.close()    
    

    
    
    