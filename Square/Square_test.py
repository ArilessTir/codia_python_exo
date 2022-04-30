import unittest
from Square import Square

class SquareTestCase(unittest.TestCase):
    def test_real_numbers(self):
        self.assertEqual(Square(5), 25)

    def test_zero(self):
        self.assertEqual(Square(0), 0)

    def test_negatif_numbers(self):
        self.assertEqual(Square(-10), 100)

if __name__ == '__main__':
    unittest.main()