import flask_wtf
import wtforms


class FormLogin(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Sing in")
