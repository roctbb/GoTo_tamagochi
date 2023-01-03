class Animal:
    def __init__(self):
        self.__hunger = None
        self.__health = None
        self.__mood = None
        self.__timer = None

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
        raise NotImplementedError

    def wash(self):
        raise NotImplementedError

    def play(self):
        raise NotImplementedError

    def is_alive(self):
        raise NotImplementedError
