import unittest
from translator import *

tr = instantiate_translator()

class TestTranslation(unittest.TestCase):
    def test_e2f_equal(self):
        self.assertEqual(
            english_to_french(tr, "Hello")['translations'][0]['translation'],
            "Bonjour")

    def test_e2f_is_null(self):
        self.assertEqual(english_to_french(tr, None), "Please include a sentence to translate.")

    def test_f2e_equal(self):
        self.assertEqual(
            french_to_english(tr, "Bonjour")['translations'][0]['translation'],
            "Hello")

    def test_f2e_is_null(self):
        self.assertEqual(french_to_english(tr, None), "Please include a sentence to translate.")

if __name__ == '__main__':
    unittest.main()