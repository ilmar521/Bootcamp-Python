
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(''.join(self.animals))

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        # unpacking
        animals_temp = []
        for i in (len(self.animals)):
            if type(i) is list:
                for x in i:
                    animals_temp.append(x)
            else:
                animals_temp.append(i)
        animals_temp.sort()



