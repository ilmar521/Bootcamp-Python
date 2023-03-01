
class Airline:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

class Airplane:
    ID = 0

    def __init__(self, current_location, company):
        self.id = Airplane.ID
        self.current_location = current_location
        if self not in current_location.planes:
            current_location.planes.append(self)
        self.company = company
        if self not in company.planes:
            company.planes.append(self)
        self.next_flights = []
        Airplane.ID += 1

