import unittest
from regex_to_dfa import RegexToDFA

class TestRegexToDFA(unittest.TestCase):
    def setUp(self):
        self.dfa = RegexToDFA("(a|b)*abb")
        
    def test_accepts_valid_string(self):
        self.assertTrue(self.dfa.accepts("aabb"))
        self.assertTrue(self.dfa.accepts("abb"))
        self.assertTrue(self.dfa.accepts("babb"))
        
    def test_rejects_invalid_string(self):
        self.assertFalse(self.dfa.accepts("ababa"))
        self.assertFalse(self.dfa.accepts("aab"))
        self.assertFalse(self.dfa.accepts("baa"))

if __name__ == "__main__":
    unittest.main()
