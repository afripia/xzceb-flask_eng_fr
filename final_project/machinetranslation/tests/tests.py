import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(english_to_french('Hello, how are you today?'))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(french_to_english('Bonjour, comment vous êtes aujourd\'hui?'))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()