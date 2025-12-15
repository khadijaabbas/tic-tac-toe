'''
This code implements a game of tic-tac-toe, allowing the player to play 
against the computer. It checks for winning conditions, ties and ensures that
the game runs smoothly.

Overall, it provides a fun and efficent tic-tac-toe experience, demonstarting 
core python concepts.
'''


import random
import os

# Setup output file (same folder)
output_path = "output.txt"

# Try reading previous winner
try:
    with open(output_path, "r") as file:
        print("\nPrevious Winner:")
        print(file.read())
except FileNotFoundError:
    print("No previous winner file found. Continuing game...\n")

# Initialize the game
board = ["-"] * 9
current_player = "X"
winner = None
game_running = True

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def input_player(board):
    global current_player
    try:
        input1 = int(input("Enter a number between 1 and 9: "))
        if 1 <= input1 <= 9 and board[input1-1] == "-":
            board[input1-1] = current_player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is taken or invalid!")
    except ValueError:
        print("Please enter a valid number.")

def horizontal(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True

def vertical(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True

def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True

while game_running:
    print_board(board)
    input_player(board)

    # Check for win or tie
    if horizontal(board) or vertical(board) or diagonal(board):
        print_board(board)
        print(f"{winner} wins!")
        with open(output_path, "w") as file:
            file.write(winner)
        game_running = False
    elif "-" not in board:
        print_board(board)
        print("It's a tie!")
        with open(output_path, "w") as file:
            file.write("Tie")
        game_running = False

        
    

    
    
    
