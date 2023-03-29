from app import db
import datetime


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    gender = db.Column(db.String(1))
    breed = db.Column(db.String(150))
    date_of_birth = db.Column(db.Text)
    details = db.Column(db.DateTime, default=datetime.datetime.now())
    price = db.Column(db.Integer)
    image = db.Column(db.String(250))
    cart = db.Column(db.Integer, db.ForeignKey('cart.id'))


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pets = db.relationship('Pet', backref='cart', lazy='dynamic')


