import flask
from app import flask_app, db
from app.models import User
from app.forms import FormLogin, AddForm
from flask import flash


@flask_app.route("/")
def index():
    users = {'first': list(User.query.all()),
             'second': list(User.query.filter(User.city == 'Roscoeview')),
             'third': list(User.query.limit(5).all()),
             'fourth': list(User.query.filter(User.zipcode.like('5%')))}

    return flask.render_template('index.html', users=users)


@flask_app.route("/login", methods=("GET", "POST"))
def login_page():
    my_form = FormLogin()

    if my_form.validate_on_submit():
        name = my_form.name.data
        if all(x.isalpha() or x.isspace() for x in name):
            if User.query.filter(User.name == my_form.name.data).first() is not None:
                flash('You logged in!', 'success')
                return flask.redirect(flask.url_for('login_page'))
            flash('You need to sign up!', 'error')
            return flask.redirect(flask.url_for('add_user_page'))
        else:
            flash('Bad credentials!', 'error')
    return flask.render_template("login.html", form=my_form)


@flask_app.route("/add_user", methods=("GET", "POST"))
def add_user_page():
    my_form = AddForm()

    if my_form.validate_on_submit():
        name = my_form.name.data
        street = my_form.street.data
        city = my_form.city.data
        zipcode = my_form.zipcode.data
        user_inst = User(name=name, street=street, city=city, zipcode=zipcode, status='client')
        db.session.add(user_inst)
        db.session.commit()
        return flask.redirect(flask.url_for('index'))
    return flask.render_template("add_user.html", form=my_form)

