from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.Text)
    completed = db.Column(db.Boolean)


