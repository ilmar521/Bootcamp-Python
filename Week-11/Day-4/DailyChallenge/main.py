import flask

app = flask.Flask(__name__)


@app.route('/')
def homepage():
    return flask.render_template("Homepage.html")


@app.route('/<color>')
def color_page(color):
    return flask.render_template("Color.html", color=color)


app.run()
