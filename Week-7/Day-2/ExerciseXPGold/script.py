from random import randint


def throw_dice():
    return randint(1, 6)


def throw_until_doubles():
    count_throws = 0
    while True:
        count_throws += 1
        if throw_dice() == throw_dice():
            break
    return count_throws


def main():
    list_result = []
    for i in range(0, 100):
        list_result.append(throw_until_doubles())
    print(f'Total throws: {sum(list_result)}')
    print(f'Total throws: {sum(list_result) / len(list_result)}')


main()