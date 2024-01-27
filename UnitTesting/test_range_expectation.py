import unittest
from Classes.Expectations.RangeExpectation import ExpectRange

name = "TestExpectRange"
field = "test_field"
details = {'RANGE_LWR': 0, 'RANGE_UPR': 100}


class TestExpectRangeValidation(unittest.TestCase):
    def test_validate_valid_value(self):
        expect_range = ExpectRange(name, field, details)
        expect_range.field_location = 0

        valid_row = ['50']
        expect_range.validate(1, valid_row)
        # Quick check for empty
        self.assertFalse(expect_range.errors)

    def test_validate_value_below_range(self):
        expect_range = ExpectRange(name, field, details)
        expect_range.field_location = 0

        invalid_val = '-10'
        row_num = 2

        invalid_row = [invalid_val]
        expect_range.validate(row_num, invalid_row)
        # Ensures it's not empty
        self.assertTrue(expect_range.errors)
        self.assertEqual(expect_range.errors[0].value, invalid_val)
        self.assertEqual(expect_range.errors[0].row_num, row_num)

    def test_validate_value_above_range(self):
        expect_range = ExpectRange(name, field, details)
        expect_range.field_location = 0

        invalid_val = '1000'
        row_num = 3

        invalid_row = [invalid_val]
        expect_range.validate(row_num, invalid_row)
        # Ensures it's not empty
        self.assertTrue(expect_range.errors)
        self.assertEqual(expect_range.errors[0].value, invalid_val)
        self.assertEqual(expect_range.errors[0].row_num, row_num)


if __name__ == '__main__':
    unittest.main()
