from app import db


nationality_person = db.Table('nationality_person',
    db.Column('nationality_id', db.Integer, db.ForeignKey('nationality.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')
    address = db.Column(db.String(150))
    nationalities = db.relationship("Nationality", secondary=nationality_person, back_populates="persons")


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(150))
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))


class Nationality(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    persons = db.relationship("Person", secondary=nationality_person, back_populates="nationalities")


