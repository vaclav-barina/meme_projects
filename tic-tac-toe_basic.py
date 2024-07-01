# Initial pass at tic-tac-toe

# Intialize the board
ROWS = 3
FILLER_CHAR = ' '

def initialize_board():
    board = [[' ' for _ in range(ROWS)] for _ in range(ROWS)]
    return board

# Visualize the board
def visualize_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i + 1 == len(board):
            pass
        else: 
            print("-"*9)

# Add a piece to the board
def modify_board(new_piece_location, board, player_piece):
    row_location = (new_piece_location - 1) // 3
    col_location = (new_piece_location - 1) % 3
    
    board[row_location][col_location] = player_piece
    
    return board

def check_win_condition(board): 
    # TODO: Check rows / cols
    
    # TODO: Check diags

    # Players play

    # Place piece
    # Print board state
    # Check for win condition 

# When win condition exit loop and declare winner

# End program