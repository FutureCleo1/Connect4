"""
Connect-4 Game (Human vs Computer)
State Space Search Assignment

Team Members:
- Chloe: Game Logic (Board + Moves)
- Kayla: Win Check (Goal Test)
- Gabby: AI Logic (Minimax Search Strategy)
"""
import math
import random


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
"""
def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

"""
Name: drop_piece
Function: Places a piece on the board at the specified location
parameters: board (the game board), row (the row index), col (the column index), piece (the piece to be placed, either 1 or 2)"""
def print_board(board):
    for row in reversed(board):
        print(row)

"""
Name: is_valid_location
Function: Checks if a move is valid by verifying if the top row of the specified column is empty
parameters: board (the game board), col (the column index to check)"""
def is_valid_move(board, col):
    return board[ROWS - 1][col] == 0

"""
Name: get_next_open_row
Function: Finds the next open row in a specified column where a piece can be dropped
parameters: board (the game board), col (the column index to check)
"""
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

"""
Name: drop_piece
Function: Places a piece on the board at the specified location
parameters: board (the game board), col (the column index), piece (the piece to be placed, either 1 or 2)
"""
def drop_piece(board, col, piece):
    row = get_next_open_row(board, col)
    board[row][col] = piece

"""""
Name: get_valid_moves
Function: Returns a list of valid column indices.
parameters: board (the game board)
"""
def get_valid_moves(board):
    valid_moves = []
    for col in range(COLS):
        if is_valid_move(board, col):
            valid_moves.append(col)
    return valid_moves

"""
Name: copy_board
Function: Creates a deep copy of the game board to be used in simulations (e.g., for the Minimax algorithm).
parameters: board (the game board)"""
def copy_board(board):
    return [row[:] for row in board]


# ==========================================================
# Kayla – WIN CHECK (GOAL TEST)
# ==========================================================

def check_win(board, piece):
    
    # checking for 4 in a row horizontally
    for r in range(ROWS):
        for c in range(COLS -3):
            if (board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece):

                return True
    
    # checking for 4 in a row vertically
    for c in range(COLS):
        for r in range(ROWS -3):
            if (board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece):

                return True

    # checking for 4 in a positive diagnol direction (down right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece):

                return True

    # checking for 4 in a negative diagnoal direction (up right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece):

                return True
    
    # if no connecitons found, it returns false 
    return False 
    
# ==========================================================
# Gabby – AI LOGIC (STATE SPACE SEARCH STRATEGY)
# ==========================================================

def evaluate(board, ai_piece, player_piece):
    """
    Heuristic evaluation of the board.
    Returns a score representing how favorable
    the state is for the AI.
    """
    score = 0

    # Helper function to evaluate 4-cell windows
    def evaluate_window(window):
        nonlocal score

        if window.count(ai_piece) == 4:
            score += 100
        elif window.count(ai_piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(ai_piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(player_piece) == 3 and window.count(0) == 1:
            score -= 4

    # Score center column (strategically strong)
    center_col = COLS // 2
    center_array = [board[r][center_col] for r in range(ROWS)]
    score += center_array.count(ai_piece) * 3

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            window = [board[r][c+i] for i in range(4)]
            evaluate_window(window)

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            window = [board[r+i][c] for i in range(4)]
            evaluate_window(window)

    # Positive diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)]
            evaluate_window(window)

    # Negative diagonal
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board[r-i][c+i] for i in range(4)]
            evaluate_window(window)

    return score


def minimax(board, depth, maximizing, ai_piece, player_piece):
    """
    Depth-limited Minimax algorithm.

    - board: current state
    - depth: how far to search
    - maximizing: True if AI turn, False if player turn
    """
    valid_moves = get_valid_moves(board)

    # Terminal conditions
    if check_win(board, ai_piece):
        return (None, 1000000)
    if check_win(board, player_piece):
        return (None, -1000000)
    if depth == 0 or len(valid_moves) == 0:
        return (None, evaluate(board, ai_piece, player_piece))

    if maximizing:
        max_eval = -math.inf
        best_col = random.choice(valid_moves)

        for col in valid_moves:
            temp_board = copy_board(board)
            drop_piece(temp_board, col, ai_piece)

            _, eval_score = minimax(temp_board, depth - 1, False, ai_piece, player_piece)

            if eval_score > max_eval:
                max_eval = eval_score
                best_col = col

        return best_col, max_eval

    else:
        min_eval = math.inf
        best_col = random.choice(valid_moves)

        for col in valid_moves:
            temp_board = copy_board(board)
            drop_piece(temp_board, col, player_piece)

            _, eval_score = minimax(temp_board, depth - 1, True, ai_piece, player_piece)

            if eval_score < min_eval:
                min_eval = eval_score
                best_col = col

        return best_col, min_eval



def ai_move(board, ai_piece, player_piece):
    """
    Determine the AI's move using Minimax.
    """
    depth = 4  
    col, _ = minimax(board, depth, True, ai_piece, player_piece)
    return col


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
    while True:
        choice = input("Choose your color (R/Y): ").upper()
        if choice == "R":
            player_piece = 1
            ai_piece = 2
            break
        elif choice == "Y":
            player_piece = 2
            ai_piece = 1
            break
        else:
            print("Invalid choice. Enter R or Y.")   

    # Initialize turn variable (0 = player, 1 = AI)
    turn = 0        # 0 is the player and 1 is the AI
    game_over = False

    print_board(board)

    # While the game is running:
    while not game_over:
        # If it's the player turn:
        if turn == 0:
            try:
                col = int(input("Your move (0-6): "))

                if col < 0 or col >= COLS:
                    print("Column must be between 0 and 6")
                    continue

                if is_valid_move(board, col):
                    drop_piece(board, col, player_piece)
                    print_board(board)

                    if check_win(board, player_piece):
                        print("You win!!!")
                        game_over = True
                else:
                    print("That's a invalid move. Please try again")
                    continue
            
            except ValueError:
                print("Please enter a number that's valid")
                continue

        # If it's the AI turn:
        else:
            print("It's the computer's turn")

            col = ai_move(board, ai_piece, player_piece)

            if is_valid_move(board, col):
                drop_piece(board, col, ai_piece)
                print_board(board)

                if check_win(board, ai_piece):
                    print("The Computer Wins!!!")
                    game_over = True
    
        # Switching turns
        if not game_over:
            turn = 1 - turn


if __name__ == "__main__":
    main()
   
