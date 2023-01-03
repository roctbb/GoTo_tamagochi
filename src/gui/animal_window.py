
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from domain.animal import Animal


class AnimalWindow:
    def __init__(self, animal):
        farm = Tk()
        farm.title('Tamagotchi')
def check_life():
    current_life = life.get()

    life.set(current_life - 1)

    if current_life <= 1:
        messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
        quit()
    else:
        window.after(1000, check_life)

def feed():
    life.set(100)

window = Tk()
window.title("Питомец")

life = IntVar()
life.set(50)

Progressbar(window, variable=life).pack(padx=25, pady=25)

Button(window, text="Покормить", command=feed).pack(padx=25, pady=25)

window.after(1000, check_life)

mainloop()

if __name__ == "__main__":
    animal = Animal()
    AnimalWindow(animal)
    mainloop()

