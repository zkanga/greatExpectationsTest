import csv
import json
from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.Expectations.RangeExpectation import ExpectRange
from Classes.Expectations.ValueExpectation import ExpectValues

TYPE_2_EXPECT_MAP = {
    "EXPECT_VALUES": ExpectValues,
    "EXPECT_RANGE": ExpectRange
}

DELIM = '|'


def parse_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    expectations = []
    # TODO: confirm there aren't multiple suites
    suite = config["SUITE"]["NAME"]
    GreatestExpectations.suite_name = suite
    for expect_name, details in config["SUITE"]["EXPECTATIONS"].items():
        expectations.append(TYPE_2_EXPECT_MAP[details["type"]]
                            (expect_name, details['params']['FLD_NAME'], details['params']))
    return expectations


def read_csv(input_file, delimiter, expectations):
    with open(input_file, 'r', newline='') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        # Iterate over each row in the CSV file
        for line_number, row in enumerate(csv_reader, 1):
            # print(line_number, row)
            for expectation in expectations:
                expectation.validate(line_number, row)



def validator(config, input_file_name):
    expects = parse_config(config)
    read_csv(input_file_name, DELIM, expects)


if __name__ == "__main__":
    validator(rf"test_config.json", rf"DataGen/input.csv")
