
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number = 1):
        self.animals[animal] = self.animals.get(animal, 0) + number

    def get_info(self):
        final_str = "McDonald's farm" + '\n' + '\n'
        for key, value in self.animals.items():
            final_str += f"{key} : {value}" + '\n'
        final_str += '\n\tE-I-E-I-0!'
        return final_str

    def get_animal_types(self):
        list_types = []
        for animal in self.animals.keys():
            list_types.append(animal)
        list_types.sort()
        return list_types

    def get_short_info(self):
        list_types = self.get_animal_types()
        final_str = 'McDonald’s farm has '
        if len(list_types) == 1:
            final_str += list_types[0]
        else:
            for x in range(len(list_types)):
                final_str += f'and {list_types[x]}' if x == len(list_types) - 1 else f'{list_types[x]}, '
        print(final_str)


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_short_info()
