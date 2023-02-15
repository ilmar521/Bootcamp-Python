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
            continue


def check_win():
    global game_on

    empty_field = 0
    for i in range(3):
        empty_field += board[i].count(' ')

    if empty_field <= 1:
        game_on = False
        return 'tie'

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            game_on = False
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            game_on = False
            return board[0][i]
    for val in diagonal_check:
        if board[0][val[0]] == board[1][val[1]] and board[0][val[0]] == board[2][val[2]] and board[0][val[0]] != ' ':
            game_on = False
            return board[0][val[0]]
    return ' '


def play():
    display_board()
    while game_on:
        for player in players:
            print(f"Player {player}'s turn")
            print('')
            player_input(player)
            display_board()
            winner = check_win()
            if winner != ' ':
                if winner == 'tie':
                    print(f'It is tie!')
                else:
                    print(f'Player {winner} win!')


    again = input('Do you wanna play again? (y/n): ')
    if again == 'y':
        start_game()


def start_game():
    global game_on, board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    game_on = True
    play()


print('Welcome to TIC TAC TOE!')
start_game()