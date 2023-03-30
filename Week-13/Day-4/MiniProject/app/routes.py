import flask
from app import flask_app, db
from app.models import Pet, Cart
from flask import flash


@flask_app.route("/")
def homepage():
    if len(Cart.query.all()) == 0:
        cart_inst = Cart()
        db.session.add(cart_inst)
        db.session.commit()
    return flask.render_template('homepage.html')


@flask_app.route("/pets")
def pets_page():
    return flask.render_template('pets.html', pets=list(Pet.query.all()))


@flask_app.route("/pet/<pet_id>")
def pet_details_page(pet_id):
    # list_product = list(filter(lambda product: product['ProductId'] == product_id, data))
    # return flask.render_template('product_details.html', product=list_product[0])
    pass


@flask_app.route("/cart")
def cart_page():
    pass
#     total = 0
#     for item in cart_items:
#         total += item['Price']
#     return flask.render_template('cart.html', cart_items=cart_items, total=total)


# @app.route("/add_product_to_cart/<product_id>")
# def add_product_page(product_id):
#     list_product = list(filter(lambda product: product['ProductId'] == product_id, data))
#     cart_items.append(list_product[0])
#     return flask.render_template('products.html', products=data)
#
#
# @app.route("/add_product_to_cart_from_products/<product_id>")
# def add_product_from_products(product_id):
#     list_product = list(filter(lambda product: product['ProductId'] == product_id, data))
#     cart_items.append(list_product[0])
#     return ("nothing")
#
#
# @app.route("/delete_product_from_cart/<product_id>")
# def delete_product_page(product_id):
#     list_product = list(filter(lambda product: product['ProductId'] == product_id, data))
#     cart_items.remove(list_product[0])
#     total = 0
#     for item in cart_items:
#         total += item['Price']
#     return flask.render_template('cart.html', cart_items=cart_items, total=total)


