from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.DataError import DataError


class ExpectValues(GreatestExpectations):
    exp_code = "EXPECT_VALUES"

    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.values = details['VALUES']
        self.vals_must_be = f"in {self.values}"

    def validate(self, line_number, row):
        # Choosing to optimize performance for having fewer errors
        # This is why I repeat row[self.field_location] rather than spending time to assign a variable to it
        if not row[self.field_location] in self.values:
            self.errors.append(DataError(row[self.field_location], line_number))
