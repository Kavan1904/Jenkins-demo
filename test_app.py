import unittest
from odd_even import is_even, is_odd

class TestOddEven(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))

if __name__ == '__main__':
    unittest.main()
