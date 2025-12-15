'''
This code implements a game of tic-tac-toe, allowing the player to play 
against the computer. It checks for winning conditions, ties and ensures that
the game runs smoothly.

Overall, it provides a fun and efficent tic-tac-toe experience, demonstarting 
core python concepts.
'''

import random

# Setup output file
output_path = "output.txt"

# Try reading previous winner
try:
    with open(output_path, "r") as file:
        print("\nPrevious Winner:")
        print(file.read())
except FileNotFoundError:
    print("No previous winner file found. Continuing game...\n")

# Initialize game
board = ["-"] * 9
current_player = "X"  # Human is X
winner = None
game_running = True

def print_board(board):
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def input_player(board):
    global current_player
    try:
        input1 = int(input("Enter a number between 1 and 9: "))
        if 1 <= input1 <= 9 and board[input1-1] == "-":
            board[input1-1] = current_player
        else:
            print("That spot is taken or invalid!")
            input_player(board)  # retry
    except ValueError:
        print("Please enter a valid number.")
        input_player(board)

def computer_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == "-"]
    move = random.choice(empty_spots)
    print(f"Computer chooses spot {move + 1}")
    board[move] = "O"

def check_winner():
    global winner
    # Horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            winner = board[i]
            return True
    # Vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            winner = board[i]
            return True
    # Diagonal
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    return False

# Main game loop
while game_running:
    print_board(board)

    if current_player == "X":
        input_player(board)
        current_player = "O"
    else:
        computer_move(board)
        current_player = "X"

    if check_winner():
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


        
    

    
    
    
