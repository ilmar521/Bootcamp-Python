import random


def get_random_temp(month):
    if month == 12 or month == 1 or month == 2:
        return random.uniform(-10, 16)
    elif 3 <= month <= 5:
        return random.uniform(5, 25)
    elif 6 <= month <= 8:
        return random.uniform(25, 40)
    elif 7 <= month <= 11:
        return random.uniform(5, 25)
    else:
        return random.uniform(-10, 40)


def called_main():
    month = int(input('Enter a month: '))
    temp = round(get_random_temp(month), 2)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 <= temp < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16 <= temp <= 23:
        print('Weather like early autumn')
    elif 24 <= temp <= 32:
        print('The temperature is really comfortable')
    elif 33 <= temp <= 40:
        print('So hot right now')


called_main()
