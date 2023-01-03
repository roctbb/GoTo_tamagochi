from tkinter import *

from domain.game import Game
from gui.farm_window import FarmWindow


class ModeWindow:
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.window.title("Выбор сложности")
        self.farm_window = None

        if self.game.record:
            Label(self.window, text=self.game.record, width=25, height=5).pack()
        else:
            Label(self.window, text="Вы ещё не играли.", width=25, height=5).pack()

        Button(self.window, text="Легко", width=30, height=5, command=self.__start_easy).pack()
        Button(self.window, text="Средне", width=30, height=5, command=self.__start_medium).pack()
        Button(self.window, text="Сложно", width=30, height=5, command=self.__start_hard).pack()

    def __show(self):
        self.window.deiconify()
    def __check(self):
        print(self.game.is_over())
        if self.game.is_over() and self.farm_window:
            self.farm_window.close()

    def __start_easy(self):
        self.__start_game_with_difficulty(5)

    def __start_medium(self):
        self.__start_game_with_difficulty(10)

    def __start_hard(self):
        self.__start_game_with_difficulty(20)

    def __start_game_with_difficulty(self, difficulty):
        self.window.withdraw()
        self.game.start(difficulty)
        self.farm_window = FarmWindow(self.game.farm, self.__show)


if __name__ == "__main__":
    ModeWindow(Game())

    mainloop()
