from random import randint


def compare_numbers(input_num):
    ra_number = randint(1, 100)

    if input_num == ra_number:
        print('You guess correct number!')
    else:
        print(f"Sorry, you didn't guess a number. They were {input_num} and {ra_number}")


input_num = int(input('Enter a number: '))
compare_numbers(input_num)
