import random
import time
from threading import Thread

from domain.common import get_name


class Animal:
    def __init__(self):
        self.__max_hunger = random.randint(50, 250)
        self.__hunger = self.__max_hunger
        self.__max_health = random.randint(100, 300)
        self.__health = self.__max_health
        self.__max_mood = random.randint(50, 250)
        self.__mood = self.__max_mood
        self.__name = get_name()

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
