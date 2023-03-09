from anagram_checker import AnagramChecker


def main():
    run_checker = True
    checker = AnagramChecker.create_instance()
    print("Hi! I'm anagram checker! \nYou can enter any word that you want, and I'll say you is a valid English word or not, and also show you all anargrams of this word.")
    while run_checker:
        user_input = input('\nEnter the word or just enter "q" for finish: ').strip()
        if user_input == 'q':
            run_checker = False
            print('Thanks for your time! Wait you soon.')
            continue
        if not user_input.isalpha():
            print('You entered invalid word or several words!')
            continue
        if checker.is_valid_word(user_input):
            print(f'\nYOUR WORD :”{user_input.upper()}”')
            print('this is a valid English word.')
            print(f'Anagrams for your word: {", ".join(checker.get_anagrams(user_input))}')
        else:
            print(f'\nYOUR WORD :”{user_input.upper()}”')
            print('this is not a valid English word.')


main()
