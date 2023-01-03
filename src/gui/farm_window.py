from domain.farm import Farm
from domain.animal import Animal
from animal_window import AnimalWindow
import tkinter
from tkinter import *

from domain.farm import Farm
from domain.game import Game


class FarmWindow:
    def __init__(self, farm):
        self.window = Tk()
        self.window.title('Tamagotchi')

        for animal in farm.animals:
            Button(self.window, width=12, height=2, command=lambda: self.__show_window_for(animal)).pack()

    def __show_window_for(self, animal):
        AnimalWindow(animal)



if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
