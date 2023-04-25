from flask import render_template, Blueprint
from app import flask_app, db
from app.models import Crypto
from flask_login import login_required, current_user

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    all_coins = Crypto.query.all()
    return render_template('index.html', all_coins=all_coins)


@main.route('/details/<coin_id>')
def details(coin_id):
    coin = Crypto.query.filter_by(id=coin_id).first()
    return render_template('specifics.html', coin=coin)





