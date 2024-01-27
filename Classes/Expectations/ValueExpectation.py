from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.DataError import DataError


class ExpectValues(GreatestExpectations):
    exp_code = "EXPECT_VALUES"

    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.values = details['VALUES']

    def validate(self, line_number, row):
        if not row[self.field_location] in self.values:
            self.errors.append(DataError(row[self.field_location], line_number))
