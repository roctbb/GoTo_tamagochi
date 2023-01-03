class Game:
    def __init__(self):
        self.__farm = None
        self.__points = None
        self.__record = None

    def start(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError