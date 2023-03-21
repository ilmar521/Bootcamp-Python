import flask_wtf
import wtforms
from app.validatores import my_length_should_be_lower_than_4_check, my_own_length_validator, MyOwnLengthValidator


class MyForm(flask_wtf.FlaskForm):
	username = wtforms.StringField(label="Name",
	                               validators=[wtforms.validators.DataRequired(), my_own_length_validator(2, 5)])
	mail = wtforms.StringField(label="Mail", validators=[my_length_should_be_lower_than_4_check])
	password = wtforms.PasswordField("Password", validators=[MyOwnLengthValidator(2, 6)])
	bio = wtforms.StringField("Bio")
	submit = wtforms.SubmitField("Submit")
