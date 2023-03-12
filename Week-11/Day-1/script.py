import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "HI!!"

app.run()