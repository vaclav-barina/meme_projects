# TODO: Generalize board formation 
# TODO: Add doc strings to functions
# TODO: Add checks for illegal moves. Move user input into the functions

ROWS = 3
FILLER_CHAR = ' '

def initialize_board():
    board = [[' ' for _ in range(ROWS)] for _ in range(ROWS)]
    return board

def visualize_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i + 1 == len(board):
            pass
        else: 
            print("-"*9)

def modify_board(new_piece_location, board, player_piece):
    row_location = (new_piece_location - 1) // 3
    col_location = (new_piece_location - 1) % 3
    
    board[row_location][col_location] = player_piece
    
    return board

def check_win_condition(board): 
    board_columns = [list(col) for col in zip(*board)] # Transposes the board to get a list of columns
    board_diagonals = [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    board_rows = board

    lines = board_rows + board_columns + board_diagonals

    for line in lines:
        # print(f'Line is {line}')
        if line[0] != ' ' and all(piece == line[0] for piece in line):
            return True
    
    return False 