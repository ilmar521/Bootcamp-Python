from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    street = db.Column(db.String(250))
    zipcode = db.Column(db.String(20))

