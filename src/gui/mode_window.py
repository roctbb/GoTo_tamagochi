from tkinter import *
from tkinter.messagebox import showinfo

from domain.common import storage_path
from domain.game import Game
from gui.farm_window import FarmWindow


class ModeWindow:
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.window.title("Выбор сложности")
        self.farm_window = None
        self.record_var = StringVar()

        Label(self.window, textvariable=self.record_var, width=25, height=5).pack()

        if self.game.record:
            self.record_var.set(f"Ваш рекорд: {self.game.record}")
        else:
            self.record_var.set("Вы ещё не играли.")

        Button(self.window, text="Легко", width=30, height=5, command=self.__start_easy).pack()
        Button(self.window, text="Средне", width=30, height=5, command=self.__start_medium).pack()
        Button(self.window, text="Сложно", width=30, height=5, command=self.__start_hard).pack()

        self.window.after(1000, self.tick)

    def __end(self):
        if not self.game.is_over():
            self.game.end()
        showinfo(title="Поражение", message="Вы проиграли!")
        self.record_var.set(str(f"Ваш рекорд: {self.game.record}"))
        self.window.deiconify()


    def tick(self):

        if self.farm_window and not self.game.is_over():
            self.game.tick()
            self.farm_window.tick()

        if self.game.is_over():
            if self.farm_window:
                self.farm_window.close()
                self.farm_window = None

        self.window.after(1000, self.tick)

    def __start_easy(self):
        self.__start_game_with_difficulty(5)

    def __start_medium(self):
        self.__start_game_with_difficulty(10)

    def __start_hard(self):
        self.__start_game_with_difficulty(20)

    def __start_game_with_difficulty(self, difficulty):
        self.game.start(difficulty)

        self.farm_window = FarmWindow(self.window, self.game.farm)
        self.farm_window.on_close = self.__end
        self.window.withdraw()


if __name__ == "__main__":
    ModeWindow(Game())
    mainloop()
