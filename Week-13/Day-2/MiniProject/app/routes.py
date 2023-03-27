import flask
from app import flask_app
from app import db
from app.forms import FormCV


@flask_app.route("/")
def index():
    return  flask.render_template_string('hello')

