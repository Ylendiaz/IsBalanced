import unittest
import IsBalanced

class TestStringMethods(unittest.TestCase):
    def test_IsBalanced (self):
        self.assertTrue(IsBalanced.check('[{()}]'))
    
    def test_SecondCaseIsBalanced (self):
        self.assertTrue(IsBalanced.check('[{()}]'))

    def test_IsNull(self):
        self.assertTrue(IsBalanced.check(''))

    def test_IsNotNull(self):
        self.assertFalse(IsBalanced.check('('))
    
    def test_IsNotBalanced (self):
        self.assertFalse(IsBalanced.check('({)}'))

    def test_SecondCaseIsNotBalanced(self):
        self.assertFalse(IsBalanced.check ('{([)}]'))
        