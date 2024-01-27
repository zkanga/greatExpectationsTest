import unittest
from main import validator
from DataGen.genFakeData import gen_csv

"""
Cases to add
existing, missing, or empty but existing config or input file
writing results to a location where it can't
wrong delimiter in csv
each check works with string and int
multiple checks allow in each file
"""


class TestDataValidator(unittest.TestCase):
    # CAUTION: This test suite generates and tests against larger amounts of data
    # Likely to take minutes to generate data and take 30 MB's of space per test

    def test_best_case_integration_large_dataset(self):
        out_file_name = "ideal_data.csv"
        records = 1000000
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
        self.assertTrue(first_line.endswith("data expectations suite results: SUCCESS\n"))

    def test_fail_case_large_dataset(self):
        out_file_name = "bad_data.csv"
        records = 1000000
        delimiter = '|'

        file_header = ['Runner Name', 'Classification', 'Time In Minutes']

        classification_values = ['professional', 'amateur']
        low_num_range = 5
        high_num_range = 41
        gen_csv(out_file_name, records, delimiter, file_header, classification_values, low_num_range, high_num_range)
        results = 'bad_results.txt'
        validator("ideal_test.json", out_file_name, results)

        with open(results) as f:
            first_line = f.readline()
        self.assertTrue(first_line.endswith("data expectations suite results: FAILURE\n"))


if __name__ == '__main__':
    unittest.main()
