from task2 import app
import unittest


class TestTask2(unittest.TestCase):
    @classmethod
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/run_code'

    def test_timeout(self):
        post1 = self.app.post(self.base_url, data={'code': f"from time import sleep\nsleep(10)\nprint('hi')", 'timeout': 5})
        post2 = self.app.post(self.base_url, data={'code': "print('hi')", 'timeout': 40})
        self.assertEqual("Code execution exceeded the given timeout", post1.data.decode())
        self.assertEqual('{"timeout":["Number must be between 1 and 30."]}\n', post2.data.decode())

    def test_nonePost(self):
        post1 = self.app.post(self.base_url, data={'code': None, 'timeout': 5})
        post2 = self.app.post(self.base_url, data={'code': "print('hi')", 'timeout': None})
        self.assertTrue('{"code":["This field is required."]}\n', post1.data.decode())
        self.assertTrue('{"timeout":["This field is required."]}\n', post2.data.decode())

    def test_shellTrue(self):
        post1 = self.app.post(self.base_url, data={'code': 'print()"; echo "hacked', 'timeout': 5})
        self.assertTrue('hacked' not in post1.data.decode())
