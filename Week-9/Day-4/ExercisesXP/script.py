
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

    def __init__(self, address):
        self.address = address
        self.inhabitants = []


class City:

    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        building = Building(address)
        self.buildings.append(building)
        return building

    def info(self, address):
        list_of_buildings = list(filter(lambda building: building.address == address, self.buildings))
        list_of_ages = []
        for building in list_of_buildings:
            list_of_ages.extend(list(map(lambda inhabitant: inhabitant.age, building.inhabitants)))
        print(f"Number of buildings - {len(list_of_buildings)}; mean age of the citizens - {round(sum(list_of_ages) / len(list_of_ages)) if len(list_of_ages) > 0 else 0}")


h1 = Human('H1', 18)
h2 = Human('H2', 22)
h3 = Human('H3', 13)
h4 = Human('H4', 34)
h5 = Human('H5', 56)
h6 = Human('H6', 43)
h7 = Human('H7', 55)

city = City('Nightcity')
b1 = city.construct('Main road 45')
b2 = city.construct('Main road 15')
h1.move(b1)
h2.move(b1)
h3.move(b1)
h4.move(b1)
h5.move(b1)
h6.move(b2)
h7.move(b2)

city.info('Main road 45')
city.info('Main road 15')




