import flask
from app import flask_app
from app.forms import FormCV


@flask_app.route("/", methods=("GET", "POST"))
def index():
    my_form = FormCV()

    if my_form.validate_on_submit():
        data = {
            'name': my_form.name.data,
            'profession': my_form.profession.data,
            'phone': my_form.phone.data,
            'email': my_form.email.data,
            'address': my_form.address.data,
            'LinkedIn': my_form.LinkedIn.data,
            'Github': my_form.Github.data,
            'Facebook': my_form.Facebook.data,
            'About': my_form.About.data,
            'position': my_form.position.data,
            'period': my_form.period.data,
            'responsibilities': my_form.responsibilities.data,
            'university': my_form.university.data,
            'graduate': my_form.graduate.data
        }
        return flask.render_template('CV_template.html', data=data)
    return flask.render_template('main.html', form=my_form)

