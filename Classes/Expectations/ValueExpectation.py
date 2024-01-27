from Classes.Expectations.GreatestExpectations import GreatestExpectations


class ExpectValues(GreatestExpectations):
    exp_code = "EXPECT_VALUES"

    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.values = details['VALUES']

    def validate(self, line_number, row):
        pass
