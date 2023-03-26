import flask_wtf
import wtforms


class FormCV(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    profession = wtforms.StringField("Profession", validators=[wtforms.validators.DataRequired()])
    phone = wtforms.StringField("Phone number", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("email", validators=[wtforms.validators.DataRequired(), wtforms.validators.email()])
    address = wtforms.StringField("Address", validators=[wtforms.validators.DataRequired()])
    LinkedIn = wtforms.StringField("LinkedIn link", validators=[wtforms.validators.DataRequired()])
    Github = wtforms.StringField("Github link", validators=[wtforms.validators.DataRequired()])
    Facebook = wtforms.StringField("Facebook link", validators=[wtforms.validators.DataRequired()])
    About = wtforms.TextAreaField("About", validators=[wtforms.validators.DataRequired()])
    position = wtforms.StringField("Last work position", validators=[wtforms.validators.DataRequired()])
    period = wtforms.StringField("Period of work", validators=[wtforms.validators.DataRequired()])
    responsibilities = wtforms.TextAreaField("Responsibilities", validators=[wtforms.validators.DataRequired()])
    university = wtforms.StringField("University", validators=[wtforms.validators.DataRequired()])
    graduate = wtforms.StringField("Graduation", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Create CV")
