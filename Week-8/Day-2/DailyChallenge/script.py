
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number = 0):
        if animal in self.animals.keys():
            self.animals[animal] += 1 if number == 0 else number
        else:
            self.animals[animal] = 1 if number == 0 else number

    def get_info(self):
        final_str = "McDonald's farm" + '\n' + '\n'
        for key, value in self.animals.items():
            final_str += f"{key} : {value}" + '\n'
        final_str += '\n' + '    E-I-E-I-0!'
        return final_str


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
