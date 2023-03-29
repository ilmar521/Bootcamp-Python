import flask
from app import flask_app, db
from app.models import Person, Phonenumber
from flask import flash


@flask_app.route("/")
def index():
    return flask.render_template_string('Daily challenge')


@flask_app.route("/person/<data>")
def find_data(data):
    phonenumber = Phonenumber.query.filter(Phonenumber.number == data).first()
    if phonenumber is not None:
        return flask.render_template('index.html', users=[phonenumber.person], phones=[phonenumber])
    person = Person.query.filter(Person.name == data).first()
    if person is not None:
        return flask.render_template('index.html', users=[person], phones=list(person.phonenumbers.all()))

    flash(f'Not find any data with - {data}')
    return flask.render_template('index.html')




