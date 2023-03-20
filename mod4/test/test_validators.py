import unittest
import requests
from flask_wtf import FlaskForm
from wtforms import Field

from main import number_length, NumberLength, app, RegistrationForm


class TestDecoder(unittest.TestCase):
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_validators(self):
        with app.app_context():
            response = self.app.post(self.base_url, data={
                "email": "tedt@example.com",
                "phone": "99659782221",
                "name": "Иванов Иван",
                "adress": "На деревню, дедушка",
                "index": "187110",
                "comment": "вход со двора"
            })
            self.assertTrue(
                "Successfully registered user tedt@example.com with phone +799659782221" == response.data.decode())

    def test_error(self):
        with app.app_context():
            response = self.app.post(self.base_url, data={
                "email": "tedtexample.com",
                "phone": "9965978222111",
                "name": "Иванов Иван11",
                "adress": "На деревню, дедушка",
                "index": "187110",
                "comment": "вход со двора"
            })
            self.assertTrue(
                "Successfully registered user tedt@example.com with phone +799659782221" == response.data.decode())

