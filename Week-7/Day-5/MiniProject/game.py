board = []
game_on = False
players = ['X', 'O']
board_layout = [
    ['0', '*', ' ', ' ', ' ', 0, ' ', '|', ' ', 1, ' ', '|', ' ', 2, ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*'],
    ['1', '*', ' ', ' ', ' ', 0, ' ', '|', ' ', 1, ' ', '|', ' ', 2, ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*'],
    ['2', '*', ' ', ' ', ' ', 0, ' ', '|', ' ', 1, ' ', '|', ' ', 2, ' ', ' ', ' ', '*'],
]
diagonal_check = [
    [0, 1, 2],
    [2, 1, 0]
]
winner_player = ''

def display_board():
    print('')
    print('TIC TAC TOE!')
    print('*' * 17)
    for i in range(len(board_layout)):
        list_str = board_layout[i].copy()
        if 0 in list_str:
            for n in range(0, 3):
                index = list_str.index(n)
                list_str[index] = board[int(list_str[0])][n]
            list_str.pop(0)
            print("".join(list_str))
        else:
            print("".join(list_str))
    print('*' * 17)


def player_input(player):
    while True:
        try:
            row = int(input('Enter a row: '))
            col = int(input('Enter a column: '))
            if board[row - 1][col - 1] != ' ':
                print('You choose field which already contains value!')
            else:
                board[row - 1][col - 1] = player
                break
        except Exception:
            print('You enter invalid values!')


def is_tie():
    global winner_player
    empty_field = 0 # extract this section to a function like is_tie
    for i in range(3):
        empty_field += board[i].count(' ')

    if empty_field <= 1:
        winner_player = 'tie'
        return True
    else:
        return False


def is_win_in_row():
    global winner_player
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            winner_player = board[i][0]
            return True
    return False


def is_win_in_column():
    global winner_player
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            winner_player = board[0][i]
            return True
    return False


def is_win_in_diagonal():
    global winner_player
    for val in diagonal_check:
        if board[0][val[0]] == board[1][val[1]] and board[0][val[0]] == board[2][val[2]] and board[0][val[0]] != ' ':
            winner_player = board[0][val[0]]
            return True
    return False


def check_win():
    global game_on

    if is_tie():
        game_on = False
        return

    if is_win_in_row() or is_win_in_column() or is_win_in_diagonal():
        game_on = False
    return


def play():
    display_board()
    while game_on:
        for player in players:
            print(f"Player {player}'s turn")
            print('')
            player_input(player)
            display_board()
            check_win()
            if winner_player != '':
                if winner_player == 'tie':
                    print(f'It is tie!')
                else:
                    print(f'Player {winner_player} win!')
                    break

    again = input('Do you wanna play again? (y/n): ')
    if again == 'y':
        start_game()


def start_game():
    global game_on, board, winner_player
    winner_player = ''
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    game_on = True
    play()


print('Welcome to TIC TAC TOE!')
start_game()
