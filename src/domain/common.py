import os
import random
import pathlib
import config


def get_name():
    with open(asset_path("names.txt")) as file:
        data = file.read().split('\n')
    return random.choice(data)


def get_image():
    return random.choice(list(config.IMAGES.keys()))


def asset_path(asset):
    return str(pathlib.Path(__file__).parent.resolve()) + os.sep + ".." + os.sep + "assets" + os.sep + asset
