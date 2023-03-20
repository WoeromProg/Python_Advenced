import unittest

from mod3.previous_hw_test.decoder import decoder

class TestDecoder(unittest.TestCase):
    def test_decoder(self):
        self.assertTrue(decoder("абра-кадабра.") == "абра-кадабра")
        self.assertTrue(decoder("абраа..-кадабра") == "абра-кадабра")
        self.assertTrue(decoder("абраа..-.кадабра") == "абра-кадабра")
        self.assertTrue(decoder("абра--..кадабра") == "абра-кадабра")
        self.assertTrue(decoder("абрау...-кадабра") == "абра-кадабра")
        self.assertTrue(decoder("абра........") == "")
        self.assertTrue(decoder("абр......a.") == "a")
        self.assertTrue(decoder("1..2.3") == "23")
        self.assertTrue(decoder(".") == "")
        self.assertTrue(decoder("абра-кадабра.") == "абра-кадабра")