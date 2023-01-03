from gui.mode_window import ModeWindow
from src.domain.game import Game
from tkinter import *

game = Game()
w = ModeWindow(game)
mainloop()