import flask
from app import flask_app


@flask_app.route("/")
def index():
    return flask.render_template_string('products')