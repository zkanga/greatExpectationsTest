import unittest
from main import parse_config, validate_csv

suite = parse_config("ideal_test.json")
DELIM = '|'


class TestParser(unittest.TestCase):

    def test_no_csv_file(self):
        with self.assertRaises(FileNotFoundError):
            validate_csv('does_not_exist.csv', suite, DELIM)

    def test_empty_csv_file(self):
        with self.assertRaises(StopIteration):
            validate_csv('empty.csv', suite, DELIM)

    def test_header_only_csv_file(self):
        validate_csv('header_only.csv', suite, DELIM)


if __name__ == '__main__':
    unittest.main()
