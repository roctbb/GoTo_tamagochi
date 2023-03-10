import random
from config import *

from domain.common import get_name, get_image


class Animal:
    def __init__(self):
        self.__max_hunger = random.randint(MEAN_ANIMAL_PARAM - ANIMAL_SPREAD, MEAN_ANIMAL_PARAM + ANIMAL_SPREAD)
        self.__hunger = self.__max_hunger
        self.__max_health = random.randint(MEAN_ANIMAL_PARAM - ANIMAL_SPREAD, MEAN_ANIMAL_PARAM + ANIMAL_SPREAD)
        self.__health = self.__max_health
        self.__max_mood = random.randint(MEAN_ANIMAL_PARAM - ANIMAL_SPREAD, MEAN_ANIMAL_PARAM + ANIMAL_SPREAD)
        self.__mood = self.__max_mood
        self.__name = get_name()
        self.__image = get_image()

    def tick(self):
        self.__mood -= 1
        self.__hunger -= 1
        self.__health -= 1

    @property
    def name(self):
        return self.__name

    @property
    def hunger(self):
        return self.__hunger

    @property
    def health(self):
        return self.__health

    @property
    def mood(self):
        return self.__mood

    @property
    def image(self):
        return self.__image

    @property
    def pr_max_hunger(self):
        return self.__max_hunger

    @property
    def pr_max_mood(self):
        return self.__max_mood

    @property
    def pr_max_health(self):
        return self.__max_health

    def feed(self):
        self.__hunger = self.__max_hunger

    def wash(self):
        self.__health = self.__max_health

    def play(self):
        self.__mood = self.__max_mood

    def is_alive(self):
        if self.__mood > 0 and self.__health > 0 and self.__hunger > 0:
            return True
        return False

    def is_bad(self):
        if self.__mood < self.__max_mood // 2 or self.__health < self.__max_health // 2 \
                or self.__hunger < self.__max_hunger // 2:
            return True
        return False

    @property
    def state(self):
        return "normal" if not self.is_bad() else "bad"
