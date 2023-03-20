import flask
import api_poke
from flask import request
current_page = 1

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    poke_data = api_poke.get_types_pokemon()
    if poke_data['success']:
        return flask.render_template('all_types_page.html', types=poke_data['types'])
    return flask.redirect(flask.url_for('main.html'))


@app.route("/pokemon/<id>")
def pokemon_id(id):
    poke_data = api_poke.get_pokemon(id)
    if poke_data['success']:
        return flask.render_template('pokemon.html', poke_data=poke_data)
    return flask.redirect(flask.url_for('all_types_page.html'))


@app.route("/pokemons/byname/<name>")
def pokemon_name(name):
    poke_data = api_poke.get_pokemon(name)
    if poke_data['success']:
        return flask.render_template('pokemon.html', poke_data=poke_data)
    return flask.redirect(flask.url_for('all_types_page.html'))


@app.route("/pokemons/bytype/<type>")
def pokemon_type(type):
    url_type = request.args.get('url_type')
    poke_data = api_poke.get_pokemon_by_type(url_type)
    if poke_data['success']:
        return flask.render_template('type_page.html', poke_data=poke_data['pokes'], type_name=type)
    return flask.redirect(flask.url_for('all_types_page.html'))


@app.route("/pokemons/all")
def all_pokemons():
    global current_page
    direction = request.args.get('direction')
    try:
        current_page += int(direction)
    except:
        current_page = 1

    if current_page == 0:
        current_page = 1

    poke_data = api_poke.get_all_pokemon(current_page)
    if poke_data['success']:
        return flask.render_template('all_pokemons.html', poke_data=poke_data['data'])
    return flask.redirect(flask.url_for('main.html'))


app.run(debug=True)
