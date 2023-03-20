import flask
import api_poke
from flask import request

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


app.run(debug=True)
