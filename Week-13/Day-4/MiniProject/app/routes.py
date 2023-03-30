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
    pet = Pet.query.filter(Pet.id == pet_id).first()
    return flask.render_template('pet.html', pet=pet)
    pass


@flask_app.route("/cart")
def cart_page():
    cart = Cart.query.filter(Pet.id == 1).first()
    total = 0
    pets = cart.pets.all()
    for pet in pets:
        total += pet.price
    return flask.render_template('cart.html', cart_items=pets, total=total)


@flask_app.route("/add_product_to_cart/<pet_id>")
def add_pet_page(pet_id):
    pet = Pet.query.filter(Pet.id == pet_id).first()
    pet.cart_id = 1
    db.session.add(pet)
    db.session.commit()
    flash(f'You have added {pet.name} to cart')
    return flask.render_template('pets.html', pets=list(Pet.query.all()))


@flask_app.route("/delete_pet_from_cart/<pet_id>")
def delete_pet_page(pet_id):
    pet = Pet.query.filter(Pet.id == pet_id).first()
    pet.cart_id = 0
    db.session.add(pet)
    db.session.commit()
    cart = Cart.query.filter(Pet.id == 1).first()
    total = 0
    pets = cart.pets.all()
    for pet in pets:
        total += pet.price
    return flask.render_template('cart.html', cart_items=pets, total=total)


