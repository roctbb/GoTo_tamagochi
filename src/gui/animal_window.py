from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from domain.animal import Animal


class AnimalWindow:
    def __init__(self, animal):
        self.window = Tk()
        self.window.title("Питомец")
        self.health = IntVar()
        self.health.set(animal.health)
        self.animal = animal

        Progressbar(self.window, variable=self.health).pack(padx=25, pady=25)
        Button(self.window, text="Покормить", command=self.feed).pack(padx=25, pady=25)
        Progressbar(self.window, variable=self.health).pack(padx=25, pady=25)
        Button(self.window, text="Поиграть", command=self.play).pack(padx=25, pady=25)
        self.window.after(1000, self.update)

    def update(self):
        self.health.set(self.animal.health)
        self.window.after(1000, self.update)

    def feed(self):
        self.animal.feed()

    def play(self):
        self.animal.play()


if __name__ == "__main__":
    animal = Animal()
    AnimalWindow(animal)
    mainloop()
