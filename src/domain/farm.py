from domain.animal import Animal


class Farm:
    def __init__(self, n):
        self.__animals = []

        for i in range(n):
            self.__animals.append(Animal())

    @property
    def animals(self):
        return tuple(self.__animals)

    def get_stats(self):
        """
        [
            {
                "name": "Natasha",
                "health": 100,
                "mood": 100,
                "hunger": 100
            },

        ]
        :return:
        """
        b = []
        for animal in self.__animals:
            var = {
                    'name': animal.name,
                    'hunger': animal.hunger,
                    'health': animal.health,
                    'mood': animal.mood,
                }
            b.append(var)
        return b
