from domain.common import storage_path
from domain.farm import Farm


class Game:
    def __init__(self):
        self.__farm = None
        self.__points = 0
        self.__record = None
        self.__started = False
        self.__load_record_from_storage()

    def tick(self):
        if self.__started:
            self.__points += 1
            for animal in self.__farm.animals:
                if not animal.is_alive():
                    self.end()
                    break
                animal.tick()

    def start(self, difficulty):
        self.__farm = Farm(difficulty)
        self.__started = True
        self.__points = 0

    def is_over(self):
        return not self.__started

    @property
    def points(self):
        return self.__points

    @property
    def record(self):
        return self.__record

    @property
    def farm(self):
        return self.__farm

    def __save_record_to_storage(self):
        with open(storage_path('scores.txt'), 'a') as file:
            file.write(str(self.record) + "\n")

    def __load_record_from_storage(self):
        with open(storage_path("scores.txt")) as file:
            data = file.read().split('\n')[-1]

            self.__record = int(data)

    def end(self):
        self.__started = False
        print("Game is ended")
        if not self.__record or self.__points > self.__record:
            self.__record = self.__points
            self.__save_record_to_storage()
        self.__points = 0
