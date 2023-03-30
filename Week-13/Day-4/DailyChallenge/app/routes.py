import flask
from app import flask_app, db
from app.models import Person, Phonenumber, Nationality
from flask import flash


@flask_app.route("/")
def index():
    return flask.render_template_string('Daily challenge')


@flask_app.route("/person/<data>")
def find_data(data):
    phonenumber = Phonenumber.query.filter(Phonenumber.number == data).first()
    if phonenumber is not None:
        return flask.render_template('index.html', users=[phonenumber.person], phones=[phonenumber], nationalities=phonenumber.person.nationalities)
    person = Person.query.filter(Person.name == data).first()
    if person is not None:
        return flask.render_template('index.html', users=[person], phones=list(person.phonenumbers.all()), nationalities=person.nationalities)

    flash(f'Not find any data with - {data}')
    return flask.render_template('index.html')


@flask_app.route("/people/<nationality>")
def nationality_data(nationality):
    nationality_data = Nationality.query.filter(Nationality.name == nationality).first()
    if nationality_data is not None:
        persons = list(nationality_data.persons)
        phones = []
        for person in persons:
            phones.extend(list(person.phonenumbers.all()))
        return flask.render_template('index.html', users=persons, phones=phones, nationalities=[nationality_data])

    flash(f'Not find any data with nationality - {nationality}')
    return flask.render_template('index.html')


