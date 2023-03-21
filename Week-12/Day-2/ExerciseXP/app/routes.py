import flask
from flask import app as app_new
import os
from flask import send_from_directory
from app import flask_app
from app.forms import AddCity
import json

list_of_cities = []


@flask_app.route("/")
def index():
    return flask.render_template('main.html')


@flask_app.route("/add_city", methods=("GET", "POST"))
def add_city():
    my_form = AddCity()

    if my_form.validate_on_submit():
        name = my_form.name.data
        country = my_form.country.data
        number_of_inhabitants = my_form.number_of_inhabitants.data
        area = my_form.area.data
        new_city = {
            'name': name,
            'country': country,
            'number_of_inhabitants': number_of_inhabitants,
            'area': area,
        }
        list_of_cities.append(new_city)
        filename = os.path.join(flask_app.static_folder, 'cities_around_the_world.json')
        with open(filename, 'r') as f:
            data = json.load(f)
        data.append(new_city)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return flask.redirect(flask.url_for('add_city'))

    return flask.render_template("add_city.html", form=my_form)
