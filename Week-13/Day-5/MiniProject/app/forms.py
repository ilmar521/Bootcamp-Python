import flask_wtf
import wtforms


class AddForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("ADD")
