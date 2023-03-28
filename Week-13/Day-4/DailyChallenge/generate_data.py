import faker
from app import flask_app, db
from app.models import Person, Phonenumber
import random


def generate():
    fake = faker.Faker()
    list_persons = []
    list_phones = []
    for i in range(20):
        list_persons.append(Person(name=fake.name(), email='', address=fake.address()))
    for i in range(30):
        list_phones.append(Phonenumber(number=fake.phone_number(), person=random.choice(list_persons)))

    with flask_app.app_context():
        db.session.add_all(list_persons)
        db.session.add_all(list_phones)
        db.session.commit()


generate()

