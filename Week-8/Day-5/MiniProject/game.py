import random


class Game:

    def get_user_item(self):
        list_of_values = ['r', 'p', 's']
        while True:
            value = input('Select (r)ock, (p)aper or (s)cissors: ')
            if value in list_of_values:
                return value
            else: # this else is redundant
                print('You enter invalid value, please enter again')

    def get_computer_item(self):
        return random.choice(['r', 'p', 's'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        else: # this else is redundant
            if user_item == 'r' and computer_item == 'p':
                return 'loss'
            elif user_item == 'r' and computer_item == 's': # there is no need to type elif, just if because you do return
                return 'win'
            elif user_item == 'p' and computer_item == 's':
                return 'loss'
            elif user_item == 'p' and computer_item == 'r':
                return 'win'
            elif user_item == 's' and computer_item == 'r':
                return 'loss'
            elif user_item == 's' and computer_item == 'p':
                return 'win'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        dict_values = {'r':'rock', 'p':'paper', 's':'scissors'}
        dict_results = {'win': 'You win!', 'loss': 'You lose', 'draw': 'You drew!'}
        print(f'You selected {dict_values[user_item]}. The computer selected {dict_values[computer_item]}. {dict_results[result]}')
        return result
