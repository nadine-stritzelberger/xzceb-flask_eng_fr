import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Comment'), 'How')
        self.assertEqual(french_to_english(' '), ' ')
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('How'), 'Comment')
        self.assertEqual(english_to_french(' '),' ')
    
if __name__=='__main__':
    unittest.main()