from gui.animal_window import AnimalWindow
from tkinter import *

from domain.game import Game


class FarmWindow:
    def __init__(self, parent, farm, close_handler):
        self.farm = farm
        self.window = Toplevel(parent)
        self.window.title('Tamagotchi')
        self.children = []

        for i in range(len(self.farm.animals)):
            Button(self.window, width=12, height=2, command=lambda: self.__show_window_for(self.farm.animals[i])).grid(
                row=i // 5, column=i % 5)

        self.__close_handler = close_handler
        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def __show_window_for(self, animal):
        self.children.append(AnimalWindow(self.window, animal))

    def close(self):
        #for child in self.children:
        #    child.close()
        self.window.destroy()
        self.__close_handler()

    def tick(self):
        for child in self.children:
            child.tick()


if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
