import flask

from app import flask_app
from app.forms import MyForm


@flask_app.route("/")
@flask_app.route("/products")
def products_page():
	return flask.render_template('my_template.html')


@flask_app.route("/myForm", methods=("GET", "POST"))
def myForm():
	my_form = MyForm()

	if my_form.validate_on_submit():
		username = my_form.username.data
		password = my_form.password.data
		bio = my_form.bio.data

		print(username)
		print(password)
		print(bio)

	return flask.render_template("my_from.html", form=my_form)
