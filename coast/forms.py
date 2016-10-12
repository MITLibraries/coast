from flask_wtf import Form
from wtforms import IntegerField, StringField
from wtforms.validators import Optional


class AuthorForm(Form):
    name = StringField('Name', validators=[Optional()])
    mit_id = IntegerField('MIT ID', validators=[Optional()])
