from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

db = SQLAlchemy()


def create_app():
    flask_app = Flask(__name__)

    flask_app.config.from_object(Config)
    db.init_app(flask_app)
    migrate = Migrate(flask_app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from app.auth.auth import auth as auth_blueprint
    flask_app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from app.main.main import main as main_blueprint
    flask_app.register_blueprint(main_blueprint)

    return flask_app