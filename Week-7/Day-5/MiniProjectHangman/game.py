import random

hangman = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
hangman_game = []
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = ''


def start_game():
    global word, hangman_game
    word = random.choice(wordslist)
    hangman_game = []
    print('Hide word:')
    user_word = '*' * len(word)
    user_arr = []
    print(user_word)
    while True:
        if hangman_game == hangman:
            print('Out of chances!')
            break

        user_letter = input('Enter a letter: ')
        if len(user_letter) != 1 or user_letter in user_arr:
            print('You enter the same letter or invalid value!')
            continue
        user_arr.append(user_letter)
        index_arr = []
        for index, i in enumerate(word):
            if i == user_letter:
                index_arr.append(index)

        user_arr_temp = list(user_word)
        for i in index_arr:
            user_arr_temp[i] = user_letter
        user_word = ''.join(user_arr_temp)

        if user_word == word:
            print('CONGRATS YOU WIN!')
            break
        else:
            print(user_word)
            if len(index_arr) == 0:
                for i in hangman:
                    if i not in hangman_game:
                        hangman_game.append(i)
                        break
                print(hangman_game)

start_game()