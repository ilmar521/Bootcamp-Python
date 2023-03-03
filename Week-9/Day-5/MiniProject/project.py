
class Human:
    id = 0

    def __init__(self, name, age, priority, blood_type):
        self.id_number = Human.id
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
        Human.id += 1

    def add_family_member(self, person):
        was_added = False
        if person not in self.family and person != self:
            self.family.append(person)
            was_added = True
        if self not in person.family and person != self:
            person.add_family_member(self)
            was_added = True
        if not was_added:
            return
        for human in self.family:
            human.add_family_member(person)
            person.add_family_member(human)


class Queue:

    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age >= 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def print(self):
        list_print = []
        for i in self.humans:
            list_print.append(i.name)
        print(" - ".join(list_print))

    def find_in_queue(self, person):
        for i, human in enumerate(self.humans):
            if human == person:
                return i
        print('This person is not in queue!')
        return None

    def swap(self, person1, person2):
        ind_1 = self.find_in_queue(person1)
        ind_2 = self.find_in_queue(person2)
        if ind_1 is not None and ind_2 is not None:
            self.humans[ind_2], self.humans[ind_1] = person1, person2

    def get_next(self):
        if len(self.humans) == 0:
            return None
        person = self.humans[0]
        self.humans = self.humans[1:]
        return person

    def get_next_blood_type(self, blood_type):
        list_of_blood_type = list(filter(lambda human: human.blood_type == blood_type, self.humans))
        if len(list_of_blood_type) == 0:
            return None
        person = list_of_blood_type[0]
        self.humans = [human for human in self.humans if human != person]
        return person

    def sort_by_age(self):
        list_of_priority = list(filter(lambda human: human.priority, self.humans))
        list_of_regular = list(filter(lambda human: not human.priority, self.humans))
        for x in range(len(list_of_regular)):
            for y in range(len(list_of_regular) - x - 1):
                if list_of_regular[y].age < list_of_regular[y + 1].age:
                    list_of_regular[y], list_of_regular[y + 1] = list_of_regular[y + 1], list_of_regular[y]
        self.humans = list_of_priority + list_of_regular

    # H3 - H6 - H7 - H2 - H5 - H4 - H1
    def rearange_queue(self):
        for x in range(len(self.humans)):
            for i in range(1, len(self.humans)):
                if self.humans[i - 1] in self.humans[i].family and i != len(self.humans) - 1:
                    self.humans[i], self.humans[i + 1] = self.humans[i + 1], self.humans[i]


h1 = Human('H1', 18, False, 'A')
h2 = Human('H2', 61, False, 'AB')
h3 = Human('H3', 13, True, 'B')
h4 = Human('H4', 34, False, 'AB')
h5 = Human('H5', 56, False, 'B')
h6 = Human('H6', 43, True, 'O')
h7 = Human('H7', 65, False, 'A')

queue = Queue()
queue.add_person(h1)
queue.add_person(h2)
queue.add_person(h3)
queue.add_person(h4)
queue.add_person(h5)
queue.add_person(h6)
queue.add_person(h7)

queue.print()
queue.swap(h6, h1)
queue.print()
queue.get_next()
queue.print()
queue.add_person(h7)
queue.get_next_blood_type('AB')
queue.print()
queue.add_person(h2)
queue.print()
queue.sort_by_age()
queue.print()

h3.add_family_member(h6)
h3.add_family_member(h7)
queue.rearange_queue()
queue.print()
