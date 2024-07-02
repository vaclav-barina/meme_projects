class Board():
    def __init__(self, number_rows):
        self.board_state = [[' ' for _ in range(number_rows)] for _ in range(number_rows)]
        # TODO: Refactor to be more readable
        self.board_with_labels = [[str(label) for label in range((i * number_rows) + 1, (1 + i) * number_rows + 1)] for i in range(number_rows)]
    
    def print_board(self):
        """
        Prints the current state of the tic-tac-toe board.

        The board is represented as a list of lists (2D list), where each sublist corresponds to a row on the board.
        The function prints each row, separating elements with ' | '. After each row, except the last one, it prints
        a line of dashes to visually separate the rows.

        Example:
            Assuming self.board_state is:
            [
                ['X', 'O', 'X'],
                [' ', 'X', ' '],
                ['O', ' ', 'O']
            ]

            The output will be:
            X | O | X
            ---------
              | X |  
            ---------
            O |   | O
        """
        for i, row in enumerate(self.board_state):
            print(' | '.join(row))
            if i == len(self.board_state) - 1:
                pass
            else: 
                print('-' * 9)

    # TODO: Think about seperating this out of the board class into it's own helper function
    def print_board_placement_mappings(self):
        for i, row in enumerate(self.board_with_labels):
            print(' | '.join(row))
        
            if i == len(self.board_with_labels) - 1:
                pass
            else: 
                print('-' * 9)

    def modify_board(self, player):
        print('\n See reference map below:')
        self.print_board_placement_mappings()
        new_piece_location = input(f'{player.name} select a square to input your piece: ')
        new_piece_location = int(new_piece_location) 

        row_location = (new_piece_location - 1) // 3
        col_location = (new_piece_location - 1) % 3
        
        self.board_state[row_location][col_location] = player.piece_marker
    
    # TODO: Remove hardcoded numbers assuming 3 rows
    def check_board_win_state(self):
        board_columns = [list(col) for col in zip(*self.board_state)] # Transposes the board to get a list of columns
        board_diagonals = [[self.board_state[i][i] for i in range(3)], [self.board_state[i][2 - i] for i in range(3)]]
        board_rows = self.board_state

        lines = board_rows + board_columns + board_diagonals

        for line in lines:
            # print(f'Line is {line}')
            if line[0] != ' ' and all(piece == line[0] for piece in line):
                return True
        
        return False 

    def is_board_full(self):
        return all(cell != ' ' for row in self.board_state for cell in row)

class Player():
    def __init__(self) -> None:
        self.name = input('What is your name? ')
        self.piece_marker = input('Type in a one character marker: ')