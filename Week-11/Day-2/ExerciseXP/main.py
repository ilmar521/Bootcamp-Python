import flask

app = flask.Flask(__name__)


@app.route('/')
def blog():
    return flask.render_template("index.html")


app.run()
