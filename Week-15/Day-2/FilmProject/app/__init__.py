from flask import Flask
from app.films import films
from app.accounts import accounts

flask_app = Flask(__name__)

flask_app.register_blueprint(films, url_prefix="/films")
flask_app.register_blueprint(accounts, url_prefix="/accounts")
