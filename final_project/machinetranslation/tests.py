import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Au revoir")
        self.assertEqual(englishToFrench("Goodbye"),"Au revoir")
        self.assertNotEqual(englishToFrench("Goodbye"), "Bonjour")

    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Goodbye")
        self.assertEqual(frenchToEnglish("Au revoir"),"Goodbye")
        self.assertNotEqual(frenchToEnglish("Au revoir"), "Hello")

if __name__=='__main__':
    unittest.main()



