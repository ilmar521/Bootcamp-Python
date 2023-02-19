
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        exist = False
        for str_animal in self.animals:
            if type(str_animal) is list:
                if new_animal in str_animal:
                    exist = True
            else:
                if new_animal == str_animal:
                    exist = True
        if not exist:
            self.animals.append(new_animal)

    def get_animals(self):
        final_str = []
        for str_animal in self.animals:
            if type(str_animal) is list:
                for str_animal_2 in str_animal:
                    final_str.append(str_animal_2)
            else:
                final_str.append(str_animal)

        print(','.join(final_str))

    def sell_animal(self, animal_sold):
        for str_animal in self.animals:
            if type(str_animal) is list:
                if animal_sold in str_animal:
                    str_animal.remove(animal_sold)
                    break
            else:
                if animal_sold == str_animal:
                    self.animals.remove(animal_sold)
                    break

    def sort_animals(self):
        # unpacking
        animals_temp = []
        for i in range(len(self.animals)):
            if type(self.animals[i]) is list:
                for x in self.animals[i]:
                    animals_temp.append(x)
            else:
                animals_temp.append(self.animals[i])
        animals_temp.sort()

        self.animals.clear()
        first_letter = ''
        for i in range(len(animals_temp)):
            if i + 1 == len(animals_temp):
                if first_letter == animals_temp[i][0]:
                    self.animals[-1].append(animals_temp[i])
                else:
                    self.animals.append(animals_temp[i])
            else:
                if first_letter == animals_temp[i][0]:
                    if type(self.animals[-1]) is list:
                        self.animals[-1].append(animals_temp[i])
                    else:
                        last_val = self.animals.pop()
                        self.animals.append([last_val, animals_temp[i]])
                else:
                    self.animals.append(animals_temp[i])
                first_letter = animals_temp[i][0]

    def get_groups(self):
        num_group = 0
        for str_animal in self.animals:
            if type(str_animal) is list:
                num_group += 1
                list_animal = []
                for animal in str_animal:
                    list_animal.append(animal)
                print(f'Group {num_group} - {",".join(list_animal)}')





ramat_gan_safari = Zoo('Ramat gan')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Bird')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Racoon')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Emu')

ramat_gan_safari.sort_animals()
ramat_gan_safari.add_animal('Emu')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Bird')
ramat_gan_safari.sell_animal('Something')
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()







