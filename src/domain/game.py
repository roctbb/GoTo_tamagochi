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

    def start(self):
        self.__started = True
        self.__farm = Farm(10)
        self.__points = 0

    @property
    def points(self):
        return self.__points

    @property
    def record(self):
        return self.__record

    def end(self):
        self.__started = False
        if not self.__record or self.__points > self.__record:
            print("Вау, это новый рекорд:", self.__points)
            self.__record = self.__points
        else:
            print("Мог бы лучше сыграть.")
