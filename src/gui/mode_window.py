from tkinter import *

from domain.game import Game
from gui.farm_window import FarmWindow


class ModeWindow:
    def __init__(self, game):
        self.game = game
        window = Tk()
        window.title("Выбор сложности")

        def close_window():
            quit()

        if game.record:
            Label(window, text=game.record, width=25, height=5).pack()
        else:
            Label(window, text="Вы ещё не играли.", width=25, height=5).pack()

        Button(window, text="Легко", width=30, height=5, command=self.__start_easy).pack()
        Button(window, text="Средне", width=30, height=5, command=self.__start_medium).pack()
        Button(window, text="Сложно", width=30, height=5, command=self.__start_hard ).pack()


    def __start_easy(self):
        self.__start_game_with_difficulty(5)
    def __start_medium(self):
        self.__start_game_with_difficulty(10)
    def __start_hard(self):
        self.__start_game_with_difficulty(20)

    def __start_game_with_difficulty(self, difficulty):
        self.game.start(difficulty)
        FarmWindow(self.game.farm)

if __name__ == "__main__":
    ModeWindow(Game())

    mainloop()
