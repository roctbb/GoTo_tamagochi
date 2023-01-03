from animal import Animal
class Farm:
    def __init__(self, n):
        self.__animals = []



    def get_animal(self, n):
        raise NotImplementedError

    def get_stats(self):
        """
        [
            {
                "name": "Natasha",
                "health": 100,
                "mood": 100,
                "hunger": 100
            }
        ]
        :return:
        """
        raise NotImplementedError
