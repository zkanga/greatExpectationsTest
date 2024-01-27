from Classes.Expectations.GreatestExpectations import GreatestExpectations


class ExpectValues(GreatestExpectations):
    exp_code = "EXPECT_VALUES"

    def __init__(self, suite, name, details):
        super().__init__(suite, name)

    def validate(self, row, row_number, value):
        pass
