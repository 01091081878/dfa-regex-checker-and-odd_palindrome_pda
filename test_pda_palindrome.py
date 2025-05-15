import unittest
from pda_palindrome import PDA

class TestPDA(unittest.TestCase):
    def setUp(self):
        self.pda = PDA()
        
    def test_palindromes(self):
        self.assertTrue(self.pda.is_palindrome_odd("racecar"))
        self.assertTrue(self.pda.is_palindrome_odd("madam"))
        self.assertTrue(self.pda.is_palindrome_odd("a"))
        
    def test_not_palindromes(self):
        self.assertFalse(self.pda.is_palindrome_odd("abba"))  
        self.assertFalse(self.pda.is_palindrome_odd("hello"))
        self.assertFalse(self.pda.is_palindrome_odd("abc"))

if __name__ == "__main__":
    unittest.main()
