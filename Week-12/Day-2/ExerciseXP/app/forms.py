import flask_wtf
import wtforms


class AddCity(flask_wtf.FlaskForm):
    name = wtforms.StringField("City’s name", validators=[wtforms.validators.DataRequired()])
    country = wtforms.StringField("City’s country", validators=[wtforms.validators.DataRequired()])
    number_of_inhabitants = wtforms.IntegerField("Number of inhabitants", validators=[wtforms.validators.DataRequired()])
    area = wtforms.FloatField("City’s area", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Add new city")
