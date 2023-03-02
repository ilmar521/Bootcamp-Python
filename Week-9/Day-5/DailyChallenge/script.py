import datetime

class Airline:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

    def __repr__(self):
        return self.name

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
        list_of_flights = list(filter(lambda flight: flight.destination == destination, self.next_flights))
        if len(list_of_flights) == 0:
            print("This plane doesn't have flights to this destination!")
        else:
            list_of_flights[0].take_off()
            list_of_flights[0].land()
            self.next_flights.pop(self.next_flights.index(list_of_flights[0]))

    def location_on_date(self, date):
        list_of_flights = list(filter(lambda flight: flight.date <= date, self.next_flights))
        if len(list_of_flights) == 0:
            return self.current_location
        return list_of_flights[-1].destination

    def available_on_date(self, date, location):
        location_on_date = self.location_on_date(date)
        if location_on_date != location:
            return False
        list_of_flights = list(filter(lambda flight: flight.date == date, self.next_flights))
        return len(list_of_flights) == 0


class Flight:

    def __init__(self, date:datetime.date, destination, origin, plane):
        self.ID = destination.city + plane.company.id + str(date)
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane

    def take_off(self):
        self.plane.current_location = None
        self.origin.scheduled_departures.pop(self.origin.scheduled_departures.index(self))

    def land(self):
        self.plane.current_location = self.destination
        self.destination.scheduled_arrivals.pop(self.destination.scheduled_arrivals.index(self))

    def __repr__(self):
        return self.ID

class Airport:

    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, date_time, companies):
        create_flight = False
        for company in companies:
            if create_flight:
                break
            for plane in company.planes:
                if plane.available_on_date(date_time, self):
                    new_flight = Flight(date_time, destination, self, plane)
                    self.scheduled_departures.append(new_flight)
                    destination.scheduled_arrivals.append(new_flight)
                    plane.next_flights.append(new_flight)
                    self.scheduled_departures.sort(key=lambda flight: flight.date)
                    destination.scheduled_arrivals.sort(key=lambda flight: flight.date)
                    plane.next_flights.sort(key=lambda flight: flight.date)
                    create_flight = True
                    break
        if not create_flight:
            print(f'There are not available planes with following parameters! (departure:{self.city}; destination:{destination.city}; date:{date_time})')

    def info(self, start_date, end_date):
        list_of_departures = list(filter(lambda flight: start_date <= flight.date <= end_date, self.scheduled_departures))
        list_of_arrivals = list(filter(lambda flight: start_date <= flight.date <= end_date, self.scheduled_arrivals))
        print(f"Airport {self.city} schedule:")
        print('Departures')
        if len(list_of_departures) > 0:
            for flight in list_of_departures:
                print(f"Date - {flight.date}; Destination - {flight.destination}; Company - {flight.plane.company}")
        else:
            print('no departures')

        print('Arrivals')
        if len(list_of_arrivals) > 0:
            for flight in list_of_arrivals:
                print(f"Date - {flight.date}; Destination - {flight.origin}; Company - {flight.plane.company}")
        else:
            print('no arrivals')

    def __repr__(self):
        return self.city


avrora_air = Airline('AA', 'Avrora Airlines')
elal_air = Airline('EA', 'ElAl Airlines')
list_companies = [avrora_air, elal_air]

ben_gurion = Airport('Tel Aviv')
shremetevo = Airport('Moscow')
jfk = Airport('New York')

aa_1 = Airplane(ben_gurion, avrora_air)
aa_2 = Airplane(shremetevo, avrora_air)
aa_3 = Airplane(shremetevo, avrora_air)
ea_1 = Airplane(jfk, elal_air)
ea_2 = Airplane(ben_gurion, elal_air)
ea_3 = Airplane(shremetevo, elal_air)

ben_gurion.schedule_flight(shremetevo, datetime.date(2023, 3, 4), list_companies)
ben_gurion.schedule_flight(shremetevo, datetime.date(2023, 3, 7), list_companies)
ben_gurion.schedule_flight(jfk, datetime.date(2023, 3, 5), list_companies)
shremetevo.schedule_flight(ben_gurion, datetime.date(2023, 3, 5), list_companies)
ben_gurion.schedule_flight(shremetevo, datetime.date(2023, 3, 6), list_companies)
shremetevo.schedule_flight(jfk, datetime.date(2023, 3, 3), list_companies)
shremetevo.schedule_flight(jfk, datetime.date(2023, 3, 8), list_companies)
jfk.schedule_flight(shremetevo, datetime.date(2023, 3, 4), list_companies)
jfk.schedule_flight(shremetevo, datetime.date(2023, 3, 9), list_companies)
jfk.schedule_flight(ben_gurion, datetime.date(2023, 3, 6), list_companies)

ben_gurion.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))
shremetevo.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))
jfk.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))

aa_1.fly(shremetevo)
aa_2.fly(jfk)
aa_1.fly(ben_gurion)
ea_1.fly(shremetevo)

ben_gurion.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))
shremetevo.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))
jfk.info(datetime.date(2023, 3, 1), datetime.date(2023, 3, 10))


