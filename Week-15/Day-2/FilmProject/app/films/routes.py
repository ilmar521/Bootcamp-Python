import flask

from app.films import films


@films.route("/")
def login():
    return flask.render_template("films.html")
