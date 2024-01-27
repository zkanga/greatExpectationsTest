import csv
import json
from Classes.Expectations.RangeExpectation import ExpectRange
from Classes.Expectations.ValueExpectation import ExpectValues

TYPE_2_EXPECT_MAP = {
    "EXPECT_VALUES": ExpectValues,
    "EXPECT_RANGE": ExpectRange
}


def read_csv(input_file, delimiter=','):
    with open(input_file, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        data = list(reader)
        data = {key: list(map(lambda d: d[key], data)) for key in data[0]}

    return data


def parse_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    expectations = []
    # TODO: confirm there aren't multiple suites
    suite = config["SUITE"]["NAME"]
    for expect_name, details in config["SUITE"]["EXPECTATIONS"].items():
        TYPE_2_EXPECT_MAP[details["type"]](suite, expect_name, details['params'])
    return expectations


if __name__ == "__main__":
    parse_config(rf"test_config.json")
