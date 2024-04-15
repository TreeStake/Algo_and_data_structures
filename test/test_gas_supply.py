import unittest
import os
from Algo_and_data_structures.src.gas_supply import gas_supply


class TestGasSupply(unittest.TestCase):
    def test_gas_supply(self):
        current_directory = os.path.dirname(__file__)
        resources_dir = os.path.join(current_directory, "resources", "lab_gas_supply", )
        input_file_path = os.path.join(resources_dir, "input_1.txt")
        output_file_path = os.path.join(resources_dir, "output_1.txt")

        gas_supply(input_file_path, output_file_path)

        with open(output_file_path, "r", encoding="utf-8") as file:
            output = file.readlines()
            print(output)
            expected_output = ["['Kovel', ['Novovolynsk']]\n", "['Lutsk', ['Kovel', 'Novovolynsk']]\n",
                               "['Horohiv', ['Kovel', 'Lutsk', 'Novovolynsk']]\n",
                               "['Novovolynsk', ['Kovel', 'Lutsk']]\n",
                               "['Lviv', ['Kovel', 'Lutsk', 'Horohiv', 'Novovolynsk']]\n",
                               "['Struy', ['Kovel', 'Lutsk', 'Horohiv', 'Novovolynsk', 'Lviv']]\n",
                               "['Hodoriv', ['Kovel', 'Lutsk', 'Horohiv', 'Novovolynsk', 'Lviv', 'Struy']]\n"]
        self.assertEqual(expected_output, output)

    def test_gas_supply_full_connection(self):
        current_directory = os.path.dirname(__file__)
        resources_dir = os.path.join(current_directory, "resources", "lab_gas_supply", )
        input_file_path = os.path.join(resources_dir, "input_2.txt")
        output_file_path = os.path.join(resources_dir, "output_2.txt")
        gas_supply(input_file_path, output_file_path)
        with open(output_file_path, "r", encoding="utf-8") as file:
            output = file.readlines()
            print(output)
            expected_output = ["['Kovel', []]\n", "['Lutsk', []]\n", "['Horohiv', []]\n"]
        self.assertEqual(expected_output, output)

    def test_gas_supply_connection(self):
        current_directory = os.path.dirname(__file__)
        resources_dir = os.path.join(current_directory, "resources", "lab_gas_supply", )
        input_file_path = os.path.join(resources_dir, "input_3.txt")
        output_file_path = os.path.join(resources_dir, "output_3.txt")
        gas_supply(input_file_path, output_file_path)
        with open(output_file_path, "r", encoding="utf-8") as file:
            output = file.readlines()
            print(output)
            expected_output = ["['Kyiv', []]\n", "['Kharkiv', ['Kyiv']]\n",
                               "['Odessa', ['Kyiv', 'Kharkiv']]\n",
                               "['Dnipro', ['Kyiv', 'Kharkiv', 'Odessa']]\n",
                               "['Lviv', ['Kyiv', 'Kharkiv', 'Odessa', 'Dnipro']]\n",
                               "['Zaporizhzhia', ['Kyiv', 'Kharkiv', 'Odessa', 'Dnipro', 'Lviv']]\n",
                               "['Vinnytsia', ['Kyiv', 'Kharkiv', 'Odessa', 'Dnipro', 'Lviv', 'Zaporizhzhia']]\n"]
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
