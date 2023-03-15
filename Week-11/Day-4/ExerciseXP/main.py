import flask
import database_manager

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    return flask.render_template('homepage.html')


@app.route("/products")
def products_page():
    return flask.render_template('products.html')


@app.route("/products/<product_id>")
def product_details_page(product_id):
    return flask.render_template('product_details.html')


app.run()
