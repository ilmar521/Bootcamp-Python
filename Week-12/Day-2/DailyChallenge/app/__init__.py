import flask
from config import Config

flask_app = flask.Flask(__name__)
flask_app.config.from_object(Config)

from app import routes