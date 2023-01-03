from threading import Thread
import time
from domain.farm import Farm


class Game:
    def __init__(self):
        self.__farm = None
        self.__points = None
        self.__record = None
        self.__started = False
        self.__timer = Thread(target=self.__worker)
        self.__timer.start()

    def __worker(self):
        while True:
            if self.__started:
                for animal in self.__farm.animals:

                    if not animal.is_alive():
                        self.end()
                        break

                    animal.tick()
            time.sleep(1)

    def start(self, difficulty):
        self.__farm = Farm(difficulty)
        self.__started = True
        self.__points = 0

        while self.__started:
            print(self.__farm.get_stats())
            time.sleep(1)

    @property
    def points(self):
        return self.__points

    @property
    def record(self):
        return self.__record

    @property
    def farm(self):
        return self.__farm


    def end(self):
        self.__started = False
        if not self.__record or self.__points > self.__record:
            print("Вау, это новый рекорд:", self.__points)
            self.__record = self.__points
        else:
            print("Мог бы лучше сыграть.")
