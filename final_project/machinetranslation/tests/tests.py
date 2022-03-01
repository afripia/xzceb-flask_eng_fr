import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('Hello, how are you today?'), 'Hi, how are you?')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('Bonjour, comment vous êtes aujourd\'hui?'), 'Comment vous êtes aujourd\'hui?')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()