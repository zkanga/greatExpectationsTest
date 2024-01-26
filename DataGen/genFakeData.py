import csv
from faker import Faker
from random import randint, choice

fake = Faker()

out_file_name = "input.csv"
num_records = 10
delim = '|'

header = ['Runner Name', 'Classification', 'Time In Minutes']

runner_types = ['professional', 'amateur']
low_num = 5
high_num = 40


def gen_csv(filename, num_runners):
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=delim)
        writer.writerow(header)
        for x in range(num_runners):
            # runner_data = gen_record()
            # writer.writerow(runner_data)
            writer.writerow(gen_record())

    print(f"Wrote {num_runners} to '{filename}'")


def gen_record():
    # name = fake.name()
    # classification = choice(runner_types)
    # minutes = randint(low_num, high_num)
    # return [name, classification, minutes]
    return [fake.name(), choice(runner_types), randint(low_num, high_num)]


if __name__ == "__main__":
    gen_csv(out_file_name, num_records)
