class GreatestExpectations:
    suite_name = None

    def __init__(self, name, field):
        self.expect_name = name
        self.field_name = field
        self.field_location = None
        self.errors = []

    def validate(self, line_number, row):
        pass
