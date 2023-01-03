from domain.farm import Farm


class Game:
    def __init__(self):
        self.__farm = None
        self.__points = None
        self.__record = None

    def start(self):
        self.__farm = Farm(10)
        self.__points = 0



    @property
    def points(self):
        return self.__points

    def end(self):
        if not self.__record or self.__points > self.__record:
            print("Вау, это новый рекорд:", self.__points)
            self.__record = self.__points
        else:
            print("Мог бы лучше сыграть.")
