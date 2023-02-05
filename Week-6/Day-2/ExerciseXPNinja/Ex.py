
longest_word = 0

while 1 == 1:
    word = input('Enter word without any A characters ')
    if word.capitalize().find('A') == -1:
        if len(word) > longest_word:
            longest_word = len(word)
            print('Congrats! You can find new longest word')