import unittest
from main import validator
from DataGen.genFakeData import gen_csv

###
# CAUTION READ BELOW
###

# CAUTION: This test suite generates and tests against larger amounts of data
# Likely to take minutes to generate data and take 30 MB's of space per test


# Shared data generation parameters
records = 1000000
delimiter = '|'

file_header = ['Runner Name', 'Classification', 'Time In Minutes']

classification_values = ['professional', 'amateur']
low_num_range = 5


class TestDataValidator(unittest.TestCase):

    def test_best_case_integration_large_dataset(self):
        out_file_name = "big_ideal_data.csv"
        high_num_range = 40
        gen_csv(out_file_name, records, delimiter, file_header, classification_values, low_num_range, high_num_range)
        results = 'ideal_results.txt'
        validator("ideal_test.json", out_file_name, results)

        with open(results) as f:
            first_line = f.readline()
        self.assertTrue(first_line.endswith("data expectations suite results: SUCCESS\n"))

    def test_fail_case_large_dataset(self):
        out_file_name = "big_bad_data.csv"

        high_num_range = 41
        gen_csv(out_file_name, records, delimiter, file_header, classification_values, low_num_range, high_num_range)
        results = 'bad_results.txt'
        validator("ideal_test.json", out_file_name, results)

        with open(results) as f:
            first_line = f.readline()
        self.assertTrue(first_line.endswith("data expectations suite results: FAILURE\n"))


if __name__ == '__main__':
    unittest.main()
