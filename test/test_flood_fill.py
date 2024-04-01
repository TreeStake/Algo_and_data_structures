import unittest
import os
from Algo_and_data_structures.src.flood_fill import recolor_field_from_file


class TestFloodFill(unittest.TestCase):
    def test_recolour_field_from_file_10x10(self):
        current_directory = os.path.dirname(__file__)
        input_file = os.path.join(current_directory, 'resources', 'input_1.txt')
        expected_output_file = os.path.join(current_directory, 'resources', 'output_1.txt')
        output = recolor_field_from_file(input_file)

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_lines = expected_output_file.readlines()
            expected_output = [eval(row) for row in expected_output_lines]
        self.assertEqual(output, expected_output)

    def test_recolour_field_from_file_5x5(self):
        current_directory = os.path.dirname(__file__)
        input_file = os.path.join(current_directory, 'resources', 'input_2.txt')
        expected_output_file = os.path.join(current_directory, 'resources', 'output_2.txt')
        output = recolor_field_from_file(input_file)

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_lines = expected_output_file.readlines()
            expected_output = [eval(row) for row in expected_output_lines]
        self.assertEqual(output, expected_output)

    def test_recolour_field_from_file_2x2(self):
        current_directory = os.path.dirname(__file__)
        input_file = os.path.join(current_directory, 'resources', 'input_3.txt')
        expected_output_file = os.path.join(current_directory, 'resources', 'output_3.txt')
        output = recolor_field_from_file(input_file)

        with open(expected_output_file, "r", encoding="utf-8") as expected_output_file:
            expected_output_lines = expected_output_file.readlines()
            expected_output = [eval(row) for row in expected_output_lines]
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()