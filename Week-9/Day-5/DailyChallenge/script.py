import datetime


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

    def fly(self, destination):
        pass

    def location_on_date(self, date):
        pass

    def available_on_date(self, date, location):
        pass


class Flight:

    def __init__(self, date:datetime.date, destination, origin, plane):
        self.ID = destination.city + plane.company.id + str(date)
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def take_off(self):
        pass

    def land(self):
        pass

class Airport:

    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, date_time):
        pass

    def info(self, start_date, end_date):
        pass


avrora_air = Airline('AA', 'Avrora Airlines')
elal_air = Airline('EA', 'ElAl Airlines')

ben_gurion = Airport('Tel Aviv')
shremetevo = Airport('Moscow')
jfk = Airport('New York')

aa_1 = Airplane(ben_gurion)
aa_2 = Airplane(shremetevo)
aa_3 = Airplane(shremetevo)
ea_1 = Airplane(jfk)
ea_2 = Airplane(ben_gurion)
ea_3 = Airplane(shremetevo)