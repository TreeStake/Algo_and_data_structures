import unittest
from lab_3_3 import biggest_sequence


class TestBiggestSequence(unittest.TestCase):

    def test_sorted_to_low(self):
        self.assertEquals(biggest_sequence([6, 5, 4, 3, 2, 1]), 0)

    def test_sorted_to_hight(self):
        self.assertEquals(biggest_sequence([1, 2, 3, 4, 5, 6]), 0)

    def test_two_items(self):
        self.assertEquals(biggest_sequence([1, 4]), 0)

    def test_negative_elem(self):
        self.assertEquals(biggest_sequence([1, -3, 4, 9]), 0)

    def test_biggest_sequence(self):
        self.assertEquals(biggest_sequence([2, 4, 6, 3, 1, 4, 5, 7, 3, 2, 1, 8, 5]), 7)


if __name__ == "__main__":
    unittest.main()
