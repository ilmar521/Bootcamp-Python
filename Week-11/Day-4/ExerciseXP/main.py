import flask
import database_manager

app = flask.Flask(__name__)
data = database_manager.load_database()

@app.route("/")
def homepage():
    return flask.render_template('homepage.html')


@app.route("/products")
def products_page():
    return flask.render_template('products.html', products=data)


@app.route("/products/<product_id>")
def product_details_page(product_id):
    list_product = list(filter(data, ))
    return flask.render_template('product_details.html')


app.run(debug=True)
