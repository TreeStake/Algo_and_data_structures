import unittest
from angry_cows import min_distance_between_cows


class TestMinimalPosition(unittest.TestCase):

    def test_data_lecture(self):
        self.assertEquals(min_distance_between_cows([1, 2, 8, 4, 9], 3), 3)

    def test_data_student(self):
        self.assertEquals(min_distance_between_cows([1, 2, 10, 15, 30, 42], 5), 5)


if __name__ == "__main__":
    unittest.main()
