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
    GreatestExpectations.suite_name = config["SUITE"]["NAME"]
    for expect_name, details in config["SUITE"]["EXPECTATIONS"].items():
        expectations.append(TYPE_2_EXPECT_MAP[details["type"]]
                            (expect_name, details['params']['FLD_NAME'], details['params']))
    return expectations


def read_csv(input_file, delimiter, expectations):
    with open(input_file, 'r', newline='') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        header = next(csv_reader)
        for expectation in expectations:
            expectation.field_location = header.index(expectation.field_name)
        # Iterate over each row in the CSV file
        for line_number, row in enumerate(csv_reader, 1):
            # print(line_number, row)
            for expectation in expectations:
                expectation.validate(line_number, row)


def prepare_output(expects):
    out = ""
    all_pass = True
    for expect in expects:
        curr_out, curr_result = expect.return_output()
        out += curr_out
        if not curr_result:
            all_pass = False
    if all_pass:
        message = "SUCCESS"
    else:
        message = "FAILURE"
    out = f"{GreatestExpectations.suite_name} data expectations suite results: {message}\n{out}"
    return out


def validator(config, input_file_name):
    expects = parse_config(config)
    # Pass by reference - expects updated in read_csv
    read_csv(input_file_name, DELIM, expects)
    output = prepare_output(expects)
    print(output)


if __name__ == "__main__":
    validator(rf"test_config.json", rf"DataGen/input.csv")
