import datetime

from previous_hw_test.hello_world_with_day import app
import unittest


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        username = 'nikita'
        weekday = datetime.datetime.today().weekday()
        day_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресенья')
        day = day_tuple[weekday]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day in response_text)
