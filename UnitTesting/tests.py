import unittest
from main import validator
from DataGen.genFakeData import gen_csv

"""
Cases to add
good, bad, and empty config existing and input file
writing results to a location where it can't
wrong delimiter in csv
"""


class TestDataValidator(unittest.TestCase):

    def test_best_case_integration(self):
        out_file_name = "ideal_data.csv"
        records = 100
        delimiter = '|'

        file_header = ['Runner Name', 'Classification', 'Time In Minutes']

        classification_values = ['professional', 'amateur']
        low_num_range = 5
        high_num_range = 40
        gen_csv(out_file_name, records, delimiter, file_header, classification_values, low_num_range, high_num_range)
        results = 'ideal_results.txt'
        validator("ideal_test.json", out_file_name, results)

        with open(results) as f:
            first_line = f.readline()
        self.assertTrue(first_line.endswith("suite results: SUCCESS\n"))

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
