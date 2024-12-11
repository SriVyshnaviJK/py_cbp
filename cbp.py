import numpy as np
import pandas as pd

# Function to check if the board is full
def is_board_full(board):
    return not any(' ' in row for row in board)

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    if (any(all(cell == player for cell in row) for row in board) or
        any(all(board[i][j] == player for i in range(3)) for j in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2-i] == player for i in range(3))):
        return True
    return False

# Function to print the board
def print_board(board):
    df = pd.DataFrame(board)
    print(df)

# Function to get player move
def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("That cell is already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row, col = get_player_move(board)
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        turn += 1

# Start the game
play_game()