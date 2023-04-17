import flask

from app.films import films


@films.route("/homepage")
def homepage():
    return flask.render_template("homepage.html")
