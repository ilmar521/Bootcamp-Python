import flask
import flask_sqlalchemy
import flask_migrate
import os

flask_app = flask.Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'schedule.db')

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import models, routes
