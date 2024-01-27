class GreatestExpectations:

    def __init__(self, suite, name):
        self.suite = suite
        self.expect_name = name
        self.errors = []

    def validate(self, row, row_number, value):
        pass
