import os
import random
import pathlib


def get_name():
    with open(asset_path("names.txt")) as file:
        data = file.read().split('\n')
    return random.choice(data)


def asset_path(asset):
    return str(pathlib.Path(__file__).parent.resolve()) + os.sep + ".." + os.sep + "assets" + os.sep + asset
