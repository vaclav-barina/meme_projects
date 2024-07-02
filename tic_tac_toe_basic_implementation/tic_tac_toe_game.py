from tic_tac_toe_basic import *


win_condition = False
current_player_indicator = 0

player_name = ['Player 1', 'Player 2']
player_piece_map = {'Player 1': 'X',
                    'Player 2': 'O'}

board = initialize_board()
while win_condition == False:
    
    print('Board state is:')
    visualize_board(board)

    current_player_index = current_player_indicator % 2
    current_player = player_name[current_player_index]
    player_piece = player_piece_map[current_player]

    player_input = int(input(f'{current_player} choose your location'))

    board = modify_board(player_input, board, player_piece)
    win_condition = check_win_condition(board)
    print(f'win_condition is {win_condition}')

    current_player_indicator += 1

visualize_board(board)
print(f'Game is over! {current_player} is the winner!')

    


