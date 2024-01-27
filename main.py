import csv


def read_csv(input_file, delimiter=','):
    with open(input_file, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        data = list(reader)
        data = {key: list(map(lambda d: d[key], data)) for key in data[0]}

    return data


if __name__ == "__main__":
    read_csv(rf'DataGen/input.csv', '|')
