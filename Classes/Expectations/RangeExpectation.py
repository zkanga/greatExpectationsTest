from Classes.Expectations.GreatestExpectations import GreatestExpectations


class ExpectRange(GreatestExpectations):
    exp_code = "EXPECT_RANGE"

    # TODO: confirm it works with dates
    def __init__(self, suite, name, details):
        super().__init__(suite, name)

    def validate(self, row, row_number, value):
        pass
