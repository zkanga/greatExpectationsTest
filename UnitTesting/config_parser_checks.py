import unittest
from main import parse_config
from json import decoder


class TestParser(unittest.TestCase):

    def test_no_config_file(self):
        with self.assertRaises(FileNotFoundError):
            parse_config("file_doesn't_exist.json")

    def test_bad_config_file(self):
        # Not a check for malicious users, one could swap param order
        with self.assertRaises(FileNotFoundError):
            parse_config("small_ideal_data.csv")

    def test_empty_config_file(self):
        with self.assertRaises(decoder.JSONDecodeError):
            parse_config("empty.json")

    def test_generating_correct_amount_of_suites(self):
        self.assertEqual(len(parse_config("ideal_test.json")), 2)


if __name__ == '__main__':
    unittest.main()
