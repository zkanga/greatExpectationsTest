import csv
import json
from Classes.Expectations.GreatestExpectations import GreatestExpectations
from Classes.Expectations.RangeExpectation import ExpectRange
from Classes.Expectations.ValueExpectation import ExpectValues

# Using prints as logs as of now but would add logging given time.

# Would move to config with time
TYPE_2_EXPECT_MAP = {
    "EXPECT_VALUES": ExpectValues,
    "EXPECT_RANGE": ExpectRange
}

# Would make as an env variable
DELIM = '|'
DEFAULT_OUTPUT_FILE = "results.txt"


def parse_config(config_path):
    """
    :param config_path: Path to the file specifying the configuration of the expectations in a suite
    :return: Returns an array of expectation objects based on the config file
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"ERROR: reading config file {config_path}.\n{e}")
        raise
    print(f"SUCCESS: Read config file: {config_path}")
    expectations = []
    if len(config) != 1:
        print(f"ERROR: {len(config)} suites provided, expected 1")
        exit(1)
    try:
        # Would move all the json keywords into a config file given the time
        GreatestExpectations.suite_name = config["SUITE"]["NAME"]
        for expect_name, details in config["SUITE"]["EXPECTATIONS"].items():
            expectations.append(TYPE_2_EXPECT_MAP[details["type"]]
                                (expect_name, details['params']['FLD_NAME'], details['params']))
            print(f"Generated {expect_name} expectation as a part of {GreatestExpectations.suite_name} suite")
    except KeyError:
        print(f"ERROR: Keys don't match the agreed format")
        raise
    print(f"Generated {len(expectations)} expectations as a part of {GreatestExpectations.suite_name} suite")
    return expectations


def validate_csv(input_file_path, expectation_suite, delimiter):
    """
    :param input_file_path: Path to the csv file which needs validation
    :param expectation_suite: Array of expectation objects to validate the csv
    :param delimiter: Delimiter used in the input file
    :return: None - updates tracks errors in the expectation suite by reference
    """
    try:
        with open(input_file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)

            # Updating the expectation_suite after their init is messy
            # I would refactor to generate expectations here given more time

            # Processing updating each expectation with its column number
            try:
                header = next(csv_reader)
                for expectation in expectation_suite:
                    expectation.field_location = header.index(expectation.field_name)
            except StopIteration:
                print(f"ERROR: {input_file_path} is missing a header")
                raise

            # Reading each line and then letting each expectation read it
            # Should eliminate memory impact since only a single line of the file is checked at a time
            for line_number, row in enumerate(csv_reader, 1):
                for expectation in expectation_suite:
                    # Note: As a part of validate, each expectation tracks its own errors
                    # I could log/write each error immediately to output but it'll make less organized logs
                    expectation.validate(line_number, row)
    except FileNotFoundError:
        print(f"ERROR: File '{input_file_path}' not found.")
        raise
    print(f"SUCCESS: Read all the records of {input_file_path}")


def output_data(expectation_suite, out_file):
    out = ""
    all_pass = True
    # Generating output from each expectation in the suite
    for expect in expectation_suite:
        curr_out, curr_result = expect.return_output()
        out += curr_out
        if not curr_result:
            all_pass = False
        print(f"Generated output for {expect.expect_name}")
    if all_pass:
        message = "SUCCESS"
    else:
        message = "FAILURE"
    out = f"{GreatestExpectations.suite_name} data expectations suite results: {message}\n{out}"
    print(f"Compiled all expectation results")

    try:
        with open(out_file, "w") as text_file:
            text_file.write(out)
    except Exception as e:
        print(f"Error writing to file {out_file}.\n{e}")
        raise
    print(f"SUCCESS: Wrote all expectation results to {out_file}")
    # return out


# I took the liberty of allowing writing the output file to a custom location if it was provided
# If none is provided it will output to results.txt as specified in the prompt
def validator(config_file_path, input_file_path, results_file_path=DEFAULT_OUTPUT_FILE):
    expectation_suite = parse_config(config_file_path)
    # Pass by reference - expectation_suite updated in read_csv
    validate_csv(input_file_path, expectation_suite, DELIM)
    output_data(expectation_suite, results_file_path)
    print(f"Process complete")


if __name__ == "__main__":
    validator(rf"test_config.json", rf"DataGen/input.csv")
