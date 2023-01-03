from animal import Animal
class Farm:
    def __init__(self, n):
        self.__animals = []

        for i in range(n):
            self.__animals.append(Animal())


    def get_animal(self, n):
        if n > 0 and n < len(self.__animals):
            return self.__animals

    def get_stats(self, n):
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
        for j in range(n):
            var = [
                {
                    'name': '',
                    'hunger': '',
                    'healf': '',
                    'mood': '',
                }
            ]
        raise NotImplementedError
