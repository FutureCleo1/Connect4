"""
Connect-4 Game (Human vs Computer)
State Space Search Assignment

Team Members:
- Chloe: Game Logic (Board + Moves)
- Kayla: Win Check (Goal Test)
- Gabby: AI Logic (Minimax Search Strategy)
"""
import numpy as np



# ==========================================================
# Chloe – GAME LOGIC (STATE REPRESENTATION + TRANSITIONS)
# ==========================================================
RED = (255,0,0)
YELLOW = (255,255,0)

ROWS = 6
COLS = 7

"""
Name: create_board
Function: Initialize the game board as a 2D array.
parameters: none
""""
def create_board():
    board = np.zeros((6,7))
    return board

"""
Name: drop_piece
Function: Places a piece on the board at the specified location
parameters: board (the game board), row (the row index), col (the column index), piece (the piece to be placed, either 1 or 2)"""
def print_board(board):
    print(np.flip(board, 0))

"""
Name: is_valid_location
Function: Checks if a move is valid by verifying if the top row of the specified column is empty
parameters: board (the game board), col (the column index to check)"""
def is_valid_move(board, COLS):
    return board[5][COLS] == 0

"""
Name: get_next_open_row
Function: Finds the next open row in a specified column where a piece can be dropped
parameters: board (the game board), col (the column index to check)
""""
def get_next_open_row(board, COLS):
    for r in range(ROWS):
        if board[r][COLS] == 0:
            return r

"""
Name: drop_piece
Function: Places a piece on the board at the specified location
parameters: board (the game board), col (the column index), piece (the piece to be placed, either 1 or 2)
""""
def drop_piece(board, COLS, piece):
    row = get_next_open_row(board, COLS)
    board[row][COLS] = piece

"""""
Name: get_valid_moves
Function: Returns a list of valid column indices.
parameters: board (the game board)
""""
def get_valid_moves(board):
    valid_moves = []
    for col in range(COLS):
        if is_valid_move(board, COLS):
            valid_moves.append(COLS)
    return valid_moves

"""
Name: copy_board
Function: Creates a deep copy of the game board to be used in simulations (e.g., for the Minimax algorithm).
parameters: board (the game board)"""
def copy_board(board):
    return np.copy(board)


# ==========================================================
# Kayla – WIN CHECK (GOAL TEST)
# ==========================================================

def check_win(board, piece):
    """
    Check horizontal, vertical, and both diagonals
    for 4 in a row.

    This represents the GOAL TEST.
    """
    pass


# ==========================================================
# Gabby – AI LOGIC (STATE SPACE SEARCH STRATEGY)
# ==========================================================

def evaluate(board, ai_piece, player_piece):
    """
    Heuristic evaluation of the board.
    Returns a score representing how favorable
    the state is for the AI.
    """
    pass


def minimax(board, depth, maximizing, ai_piece, player_piece):
    """
    Depth-limited Minimax algorithm.

    - board: current state
    - depth: how far to search
    - maximizing: True if AI turn, False if player turn
    """
    pass


def ai_move(board, ai_piece, player_piece):
    """
    Determine the AI's move using Minimax.
    """
    pass


# ==========================================================
# Kayla - MAIN GAME LOOP
# ==========================================================

def main():
    print("Welcome to Connect-4!")
    print("You will play against the computer.")
    print("Enter column number (0-6) to make a move.\n")

    # Create board
    board = create_board()

    # Player chooses color
    # TODO:
    # Ask user for 'R' or 'Y'
    # Assign AI the opposite color

    # TODO:
    # Initialize turn variable (0 = player, 1 = AI)

    # TODO:
    # While game not over:
    #   - If player turn:
    #         get input
    #         validate move
    #         drop piece
    #         check for win
    #   - If AI turn:
    #         call ai_move()
    #         drop piece
    #         check for win
    #   - Switch turns


if __name__ == "__main__":
    main()
