import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'g7hk23knbs9l;n6fsf52adc'

from app import routes