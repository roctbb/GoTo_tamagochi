from animal import Animal


class Farm:
    def __init__(self, n):
        self.__animals = []

        for i in range(n):
            self.__animals.append(Animal())

    @property
    def animals(self):
        return tuple(self.__animals)

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
        for animal in self.__animals:
            var = [
                {
                    'name': animal.name,
                    'hunger': a,
                    'health': Animal.health,
                    'mood': Animal.mood,
                }
            ]
        raise NotImplementedError
