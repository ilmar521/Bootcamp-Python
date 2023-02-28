
class Human:

    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        if self not in building.inhabitants:
            building.inhabitants.append(self)


class Building:

    def __init__(self, address, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants

class City:

    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        self.buildings.append(Building(address))

    def info(self, address):
        list_of_buildings = list(filter(lambda building: building.address == address, self.buildings))
        list_of_ages = []
        for building in list_of_buildings:
            list_of_ages.extend(list(map(lambda inhabitant: inhabitant.age, building.inhabitants)))
        print(f"Number of buildings - {len(list_of_buildings)}; mean age of the citizens - {sum(list_of_ages) / len(list_of_ages)}")


h1 = Human('')




