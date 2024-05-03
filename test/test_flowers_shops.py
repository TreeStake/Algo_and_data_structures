import unittest
import os
from Algo_and_data_structures.src.flowers_shops import ford_fulkerson

class TestFlowersShop(unittest.TestCase):
    def test_flowers_shops_without_connection(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_flowers_shops")
        input_file_path = os.path.join(resources_dir, "test_1.csv")
        output = ford_fulkerson(input_file_path)

        self.assertEqual(output, 0)

    def test_flowers_shops_normal_connection(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_flowers_shops")
        input_file_path = os.path.join(resources_dir, "test_2.csv")
        output = ford_fulkerson(input_file_path)

        self.assertEqual(output, 17)

    def test_flowers_shops_default_ford_fulkerson(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_flowers_shops")
        input_file_path = os.path.join(resources_dir, "test_3.csv")
        output = ford_fulkerson(input_file_path)

        self.assertEqual(output, 15)

