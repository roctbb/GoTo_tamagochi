import tkinter
from tkinter import *


farm = Tk()
farm.title('Tamagotchi')

def open_animal_state():
    state = Tk()
    state.title('Animal Information')


start = Button(farm, text="Начать игру", width=12, height=2,).pack()
animal = Button(farm, width=12, height=2, command=open_animal_state).pack()



mainloop()