from domain.farm import Farm
from domain.animal import Animal
from animal_window import AnimalWindow
import tkinter
from tkinter import *

from domain.game import Game


class FarmWindow:
    def __init__(self, farm, close_handler):
        self.farm = farm
        self.window = Tk()
        self.window.title('Tamagotchi')
        self.a = None
        for i in range(len(self.farm.animals)):
            Button(self.window, width=12, height=2, command=lambda: self.__show_window_for(self.farm.animals[i])).grid(
                row=i // 5, column=i % 5)
        self.__close_handler = close_handler
        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def __show_window_for(self, animal):
        self.a = AnimalWindow(animal)

    def close(self):
        self.window.destroy()
        self.__close_handler()


if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
