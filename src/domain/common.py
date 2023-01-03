import random


def get_name():
    with open("./assets/names.txt") as file:
        data = file.read().split('\n')
    return random.choice(data)
