import flask
from app import flask_app
from app.models import User


@flask_app.route("/")
def index():
    users = {'first': list(User.query.all()),
             'second': list(User.query.filter(User.city == 'Roscoeview')),
             'third': list(User.query.limit(5).all()),
             'fourth': list(User.query.filter(User.zipcode.like('5%')))}

    return flask.render_template('index.html', users=users)

