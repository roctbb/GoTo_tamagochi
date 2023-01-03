from tkinter import *

from domain.game import Game
from gui.farm_window import FarmWindow


class ModeWindow:
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.window.title("Выбор сложности")

        if game.record:
            Label(self.window, text=game.record, width=25, height=5).pack()
        else:
            Label(self.window, text="Вы ещё не играли.", width=25, height=5).pack()

        Button(self.window, text="Легко", width=30, height=5, command=self.__start_easy).pack()
        Button(self.window, text="Средне", width=30, height=5, command=self.__start_medium).pack()
        Button(self.window, text="Сложно", width=30, height=5, command=self.__start_hard ).pack()



    def __start_easy(self):
        self.__start_game_with_difficulty(5)
        self.window.destroy()

    def __start_medium(self):
        self.__start_game_with_difficulty(10)
        self.window.destroy()
    def __start_hard(self):
        self.__start_game_with_difficulty(20)
        self.window.destroy()

    def __start_game_with_difficulty(self, difficulty):
        self.game.start(difficulty)
        FarmWindow(self.game.farm)

if __name__ == "__main__":
    ModeWindow(Game())

    mainloop()
