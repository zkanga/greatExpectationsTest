from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.DataError import DataError


class ExpectRange(GreatestExpectations):
    exp_code = "EXPECT_RANGE"

    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.lower = details['RANGE_LWR']
        self.upper = details['RANGE_UPR']
        self.vals_must_be = f"between {self.lower} and {self.upper}"

    def validate(self, line_number, row):
        # Choosing to optimize performance for having fewer errors
        # This is why I repeat row[self.field_location] rather than spending time to assign a variable to it

        # Implementation can be retooled to work with timestamps
        if not self.lower <= int(row[self.field_location]) <= self.upper:
            self.errors.append(DataError(row[self.field_location], line_number))
