import tkinter
from tkinter import *


farm = Tk()
farm.title('Tamagotchi')

def open_animal_state():
    state = Tk()
    state.title('Animal Information')

def start_game():
    print('Choose difficulty: ')
    easy = Button(farm, width=12, height=2, command=open_game() ).pack()
    normal = Button(farm, width=12, height=2).pack()
    hard = Button(farm, width=12, height=2).pack()
    game = Tk()
    start = Button(game, text="Начать игру", width=12, height=2).pack()

start_game()


animal = Button(farm, width=12, height=2, command=open_animal_state).pack()



mainloop()