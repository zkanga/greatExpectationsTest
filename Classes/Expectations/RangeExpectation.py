from Classes.Expectations.GreatestExpectations import GreatestExpectations


class ExpectRange(GreatestExpectations):
    exp_code = "EXPECT_RANGE"

    # TODO: confirm it works with dates
    def __init__(self, name, field, details):
        super().__init__(name, field)
        self.lower = details['RANGE_LWR']
        self.upper = details['RANGE_UPR']

    def validate(self, line_number, row):
        pass
