import flask
from app import flask_app, db
from app.models import Person, Phonenumber, Nationality
from flask import flash


@flask_app.route("/")
def index():
    return flask.render_template_string('Daily challenge')


