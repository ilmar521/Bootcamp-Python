import flask
import api_poke

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    return flask.render_template('main.html')


@app.route("/pokemon/<id>")
def pokemon_id(id):
    poke_data = api_poke.get_pokemon(id)
    if poke_data['success']:
        return flask.render_template('pokemon.html', poke_data=poke_data)
    return flask.redirect(flask.url_for('homepage'))


@app.route("/pokemons/byname/<name>")
def pokemon_name(name):
    poke_data = api_poke.get_pokemon(name)
    if poke_data['success']:
        return flask.render_template('pokemon.html', poke_data=poke_data)
    return flask.redirect(flask.url_for('homepage'))


app.run(debug=True)
