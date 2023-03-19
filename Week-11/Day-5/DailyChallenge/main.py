import flask
import api_poke

app = flask.Flask(__name__)
data = products_data.load_database()
cart_items = []

@app.route("/")
def homepage():
    return flask.render_template('homepage.html')


@app.route("/pokemon/<id>")
def homepage():
    return flask.render_template('homepage.html')


app.run(debug=True)
