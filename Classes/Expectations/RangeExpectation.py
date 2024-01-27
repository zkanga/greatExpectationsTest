from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.DataError import DataError


class ExpectRange(GreatestExpectations):
    exp_code = "EXPECT_RANGE"

    # TODO: confirm it works with dates
    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.lower = details['RANGE_LWR']
        self.upper = details['RANGE_UPR']
        self.error_details = f"between {self.lower} and {self.upper}"

    def validate(self, line_number, row):
        if not self.lower <= int(row[self.field_location]) <= self.upper:
            self.errors.append(DataError(row[self.field_location], line_number))