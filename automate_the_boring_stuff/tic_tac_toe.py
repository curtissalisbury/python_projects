the_board = {'topL': ' ', 'topM': ' ', 'topR': ' ',
             'midL': ' ', 'midM': ' ', 'midR': ' ',
             'lowL': ' ', 'lowM': ' ', 'lowR': ' '
             }


def print_board(board):
    print(f'{board["topL"]}|{board["topM"]}|{board["topR"]}')
    print('-+-+-')
    print(f'{board["midL"]}|{board["midM"]}|{board["midR"]}')
    print('-+-+-')
    print(f'{board["lowL"]}|{board["lowM"]}|{board["lowR"]}')


turn = 'X'
for i in range(9):
    print_board(the_board)
    print(f'Turn for {turn}. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)

