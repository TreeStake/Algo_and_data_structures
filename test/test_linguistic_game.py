import unittest
import os
from Algo_and_data_structures.src.linguistic_game import search_chain


class TestLinguisticGame(unittest.TestCase):

    def test_search_chain_with_10(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_linguistic_game")
        input_file_path = os.path.join(resources_dir, "test_1.txt")
        output = search_chain(input_file_path)
        expected_output_file = os.path.join(resources_dir, 'output_1.txt')

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_line = expected_output_file.readline()
            expected_output = int(expected_output_line.strip())
        self.assertEqual(output, expected_output)

    def test_search_chain_with_5(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_linguistic_game")
        input_file_path = os.path.join(resources_dir, "test_2.txt")
        output = search_chain(input_file_path)
        expected_output_file = os.path.join(resources_dir, 'output_2.txt')

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_line = expected_output_file.readline()
            expected_output = int(expected_output_line.strip())
        self.assertEqual(output, expected_output)

    def test_search_chain_with_3(self):
        resources_dir = os.path.join(os.path.dirname(__file__), "resources", "lab_linguistic_game")
        input_file_path = os.path.join(resources_dir, "test_3.txt")
        output = search_chain(input_file_path)
        expected_output_file = os.path.join(resources_dir, 'output_3.txt')

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_line = expected_output_file.readline()
            expected_output = int(expected_output_line.strip())
        self.assertEqual(output, expected_output)
