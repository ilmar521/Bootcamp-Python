import random


def get_words_from_file():
    f = open('../../sowpods.txt')
    words = f.read()
    return words.split('\n')


def get_random_sentence(length):
    list_of_words = get_words_from_file()
    sentence = []
    for i in range(length + 1):
        sentence.append(random.choice(list_of_words))
    return ' '.join(sentence).lower()


def validation(length):
    if not isinstance(length, int):
        return False
    if length > 20 or length < 2:
        return False
    return True


def main():
    print('Hi! This program can create random sentence accordinly length that user enter.')
    length = int(input('Enter a length of sentence: '))
    if validation(length):
        print(get_random_sentence(length))
    else:
        print('You entered invalid value of length!')


main()
