import flask_wtf
import wtforms


class FormLogin(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Sing in")


class AddForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    street = wtforms.StringField("Street", validators=[wtforms.validators.DataRequired()])
    city = wtforms.StringField("City", validators=[wtforms.validators.DataRequired()])
    zipcode = wtforms.IntegerField("Zipcode", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Add new user")

