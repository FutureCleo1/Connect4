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
