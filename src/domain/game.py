from domain.farm import Farm


class Game:
    def __init__(self):
        self.__farm = None
        self.__points = None
        self.__record = None
        self.__started = False

    def tick(self):
        if self.__started:
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

    def end(self):
        self.__started = False
        print("Game is ended")
        if not self.__record or self.__points > self.__record:
            self.__record = self.__points
