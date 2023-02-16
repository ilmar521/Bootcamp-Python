import random

hangman = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
words_list = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']


def input_letter(user_arr):
    while True:
        user_letter = input('Enter a letter: ')
        if len(user_letter) != 1 or user_letter in user_arr:
            print('You enter the same letter or invalid value!')
            continue
        else:
            return user_letter


def compile_user_word(word, user_word, user_letter):
    index_arr = []
    for index, i in enumerate(word):
        if i == user_letter:
            index_arr.append(index)

    user_arr_temp = list(user_word)
    for i in index_arr:
        user_arr_temp[i] = user_letter
    return index_arr, ''.join(user_arr_temp)


def append_hangman(index_arr, hangman_game):
    if len(index_arr) == 0:
        for i in hangman:
            if i not in hangman_game:
                hangman_game.append(i)
                break
        print(hangman_game)


def start_game():
    word = random.choice(words_list)
    hangman_game = []
    print('Hide word:')
    user_word = '*' * len(word)
    user_arr = []
    print(user_word)
    while True:
        if hangman_game == hangman:
            print('Out of chances!')
            break

        user_letter = input_letter(user_arr)
        user_arr.append(user_letter)
        index_arr, user_word = compile_user_word(word, user_word, user_letter)
        if user_word == word:
            print('CONGRATS YOU WIN!')
            break
        else:
            print(user_word)
            append_hangman(index_arr, hangman_game)


start_game()
