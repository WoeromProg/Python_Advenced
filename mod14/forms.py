from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField
from wtforms.validators import InputRequired


class MyForm(FlaskForm):
    title = TextAreaField('Title', validators=[InputRequired()])
    author = TextAreaField('Author', validators=[InputRequired()])
