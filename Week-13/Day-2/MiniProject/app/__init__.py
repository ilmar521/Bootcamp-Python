import flask
from config import Config
import flask_sqlalchemy
import flask_migrate
import os
import json

flask_app = flask.Flask(__name__)
flask_app.config.from_object(Config)
basedir = os.path.abspath(os.path.dirname(__file__))

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'robots.db')

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import models, routes


# def populate():
#     with flask_app.app_context():
#         filename = os.path.join(flask_app.static_folder, 'users.json')
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             for user in data:
#                 user_inst = models.User(id=user['id'], name=user['name'], street=user['address']['street'], zipcode=user['address']['zipcode'])
#                 db.session.add(user_inst)
#                 db.session.commit()
#
#
# populate()