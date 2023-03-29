from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')
    address = db.Column(db.String(150))


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(150))
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))

