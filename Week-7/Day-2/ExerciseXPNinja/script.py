
str_inp = input('Enter the string: ')
list_str = str_inp.split(',')


def longest_word(arr):
    long = 0
    for x in list_str:
        if len(x) > long:
            long = len(x)
    return long


def show_frame(arr):
    maxLong = longest_word(arr)
    print("*" * (maxLong + 4))
    for x in list_str:
        if len(x) < maxLong:
            print("* " + x + " " * (maxLong - len(x)) + " *")
        else:
            print(f'* {x} *')

    print("*" * (maxLong + 4))


show_frame(list_str);
