from tic_tac_toe_basic_classes import *

NUM_ROWS = 3 

board = Board(NUM_ROWS)
players = []

print('Initialize Player 1:')
player_1 = Player()
players.append(player_1)

print('Initialize Player 2:')
player_2 = Player()
players.append(player_2)

player_count = 0

while board.check_board_win_state() is False and board.is_board_full() is False:
    current_player_index = player_count % 2
    current_player = players[current_player_index]

    'Current board state is: '
    board.print_board()

    board.modify_board(current_player)
    player_count += 1 

print('\nFinal board state is:')
board.print_board()

if board.check_board_win_state() is True:
    print(f'The winner is {current_player.name}. Congratulations!')
else:
    print('No one won. Try again later.')