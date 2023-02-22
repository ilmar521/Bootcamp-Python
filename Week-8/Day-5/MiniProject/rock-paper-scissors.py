from game import Game


def get_user_menu_choice():
    list_of_values = ['g', 'x']
    while True:
        value = input('Menu: \n (g) Play new game \n (x) Show scores and exit \n :')
        if value in list_of_values:
            return value
        else:
            print('You enter invalid value, please enter again')


def print_results(results):
    print('Game results')
    print(f' You won: {results["win"]} times')
    print(f' You lost: {results["loss"]} times')
    print(f' You drew: {results["draw"]} times')


def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            new_game = Game()
            result = new_game.play()
            results[result] += 1
        else:
            print_results(results)
            break


main()
