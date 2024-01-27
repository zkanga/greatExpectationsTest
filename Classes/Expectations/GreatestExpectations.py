class GreatestExpectations:
    suite_name = None
    exp_code = None

    def __init__(self, name, field):
        self.expect_name = name
        self.field_name = field
        self.field_location = None
        self.errors = []
        self.vals_must_be = None

    def validate(self, line_number, row):
        pass

    def return_output(self):
        if not self.errors:
            out = f"\t{self.expect_name}: PASS - All values in {self.field_name} are {self.vals_must_be}\n\n"
            result = True
        else:
            out = (f"\t{self.expect_name}: FAIL - "
                   f"{len(self.errors)} {self.exp_code} error(s) in the {self.field_name} field.\n"
                   f"\tAll values expected to be {self.vals_must_be}\n")
            for error in self.errors:
                out += f"\t\tLine {error.row_num}: Invalid value - {error.value}\n"
            result = False
        return out, result

