from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, NumberRange, Regexp, Optional, ValidationError

"""
2 Задание
"""


def number_length(min: int, max: int, message: Optional = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data < min or field.data > max:
            raise ValidationError(message)

    return _number_length


class NumberLength():
    def __init__(self, min, max, message):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):

        self.field = field.data
        if field.data < self.min or field.data > self.max:
            raise ValidationError(self.message)

"""
1 задание
"""
app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10000000000, 99999999999, "number entered incorrectly")]) # NumberRange(min=10000000000, max=99999999999)])
    name = StringField(validators=[InputRequired()])
    adress = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()

@app.route("/registration", methods=['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():

        email, phone = form.email.data, form.phone.data
        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
