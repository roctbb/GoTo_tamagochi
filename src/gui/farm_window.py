import tkinter
from tkinter import *

from domain.farm import Farm


class FarmWindow:
    def __init__(self, farm):
        self.window = Tk()
        self.window.title('Tamagotchi')


if __name__ == "__main__":
    import pathlib

    window = FarmWindow(Farm(10))
    mainloop()
