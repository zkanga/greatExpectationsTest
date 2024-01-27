import csv
from faker import Faker
from random import randint, choice

fake = Faker()


def gen_record(classifications, low_num, high_num):
    return [fake.name(), choice(classifications), randint(low_num, high_num)]


def gen_csv(filename, num_records, delim, header, classifications, low_num, high_num):
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=delim)
        writer.writerow(header)
        for x in range(num_records):
            writer.writerow(gen_record(classifications, low_num, high_num))

    print(f"Wrote {num_records} test records to '{filename}'")


if __name__ == "__main__":
    out_file_name = "input.csv"
    records = 5
    delimiter = '|'

    file_header = ['Runner Name', 'Classification', 'Time In Minutes']

    classification_values = ['professional', 'amateur']
    low_num_range = 5
    high_num_range = 40
    gen_csv(out_file_name, records, delimiter, file_header, classification_values, low_num_range, high_num_range)
