import faker
from app import flask_app, db
from app.models import Person, Phonenumber, Nationality
import random


def generate():
    # fake = faker.Faker()
    # list_persons = []
    # list_phones = []
    # for i in range(20):
    #     list_persons.append(Person(name=fake.name(), email='', address=fake.address()))
    # for i in range(30):
    #     list_phones.append(Phonenumber(number=fake.phone_number(), person=random.choice(list_persons)))
    #

    list_nationalities = []
    list_nationalities.append(Nationality(name='Israeli'))
    list_nationalities.append(Nationality(name='Russian'))
    list_nationalities.append(Nationality(name='German'))

    with flask_app.app_context():
        all_person = Person.query.all()
        for person in all_person:
            person.nationalities.append(random.choice(list_nationalities))

        db.session.add_all(list_nationalities)
        db.session.add_all(all_person)
        db.session.commit()


# generate()

