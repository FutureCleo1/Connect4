"""
Connect-4 Game (Human vs Computer)
State Space Search Assignment

Team Members:
- Chloe: Game Logic (Board + Moves)
- Kayla: Win Check (Goal Test)
- Gabby: AI Logic (Minimax Search Strategy)
"""

ROWS = 6
COLS = 7


# ==========================================================
# Chloe – GAME LOGIC (STATE REPRESENTATION + TRANSITIONS)
# ==========================================================

def create_board():
    """
    Create and return an empty 6x7 board.
    This represents the INITIAL STATE.
    """
    pass


def print_board(board):
    """
    Print the board in a user-friendly format.
    """
    pass


def is_valid_move(board, col):
    """
    Return True if move is valid, False otherwise.
    """
    pass


def drop_piece(board, col, piece):
    """
    Drop a piece into the correct row in the column.
    This represents a STATE TRANSITION.
    """
    pass


def get_valid_moves(board):
    """
    Return a list of valid column indices.
    Needed for Minimax search.
    """
    pass


def copy_board(board):
    """
    Return a deep copy of the board.
    Needed to simulate future states.
    """
    pass


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
    while True:
            player_piece = input("choose your color (R/Y): ").upper()
            if player_piece in ["R", "Y"]:
                break
            print("That's a invalid choice. Please enter R or Y")

    # Initialize turn variable (0 = player, 1 = AI)
    ai_piece = "Y" if player_piece == "R" else "R"
    turn = 0        # 0 is the player and 1 is the AI
    game_over = False

    print_board(board)

    # While the game is running:
    while not game_over:
        # If it's the player turn:
        if turn == 0:
            try:
                col = int(input("Your move (0-6): "))

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
   