import csv
from faker import Faker
from random import randint, choice

fake = Faker()

runner_types = ['professional', 'amateur']
low_num = 5
high_num = 40


def gen_record():
    # name = fake.name()
    # classification = choice(runner_types)
    # minutes = randint(low_num, high_num)
    # return [name, classification, minutes]
    return [fake.name(), choice(runner_types), randint(low_num, high_num)]


if __name__ == "__main__":
    for x in range(0, 20):
        print(gen_record())
