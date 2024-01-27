import csv
import json
from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.Expectations.RangeExpectation import ExpectRange
from Classes.Expectations.ValueExpectation import ExpectValues

# TODO: add logging

TYPE_2_EXPECT_MAP = {
    "EXPECT_VALUES": ExpectValues,
    "EXPECT_RANGE": ExpectRange
}

DELIM = '|'
DEFAULT_OUTPUT_FILE = "results.txt"

# TODO: move all the json keywords into a config file


def parse_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"ERROR: reading config file {config_path}.\n{e}")
        raise
    print(f"SUCCESS: Read config file: {config_path}")
    expectations = []
    # TODO: confirm there aren't multiple suites
    GreatestExpectations.suite_name = config["SUITE"]["NAME"]
    for expect_name, details in config["SUITE"]["EXPECTATIONS"].items():
        expectations.append(TYPE_2_EXPECT_MAP[details["type"]]
                            (expect_name, details['params']['FLD_NAME'], details['params']))
        print(f"SUCCESS: Generated {expect_name} expectation as a part of {GreatestExpectations.suite_name} suite")
    print(f"SUCCESS: Generated {len(expectations)} expectations as a part of {GreatestExpectations.suite_name} suite")
    return expectations


def read_csv(input_file, delimiter, expectations):
    try:
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
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        raise
    print(f"SUCCESS: Read all the records of {input_file}")


def output_data(expects, out_file):
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
    print(f"SUCCESS: Compiled all expectation results")
    try:
        with open(out_file, "w") as text_file:
            text_file.write(out)
    except Exception as e:
        print(f"Error writing to file {out_file}.\n{e}")
        raise
    print(f"SUCCESS: Wrote all expectation results to {out_file}")
    # return out


def validator(config, input_file_name, results_file=DEFAULT_OUTPUT_FILE):
    expects = parse_config(config)
    # Pass by reference - expects updated in read_csv
    read_csv(input_file_name, DELIM, expects)
    output_data(expects, results_file)
    print(f"SUCCESS: Process completed")


if __name__ == "__main__":
    validator(rf"test_config.json", rf"DataGen/input.csv")
