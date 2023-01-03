from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from domain.animal import Animal
from domain.game import Game


class AnimalWindow:
    def __init__(self, parent, animal):
        self.window = Toplevel(parent)
        self.window.title("Питомец")
        self.health = IntVar()
        self.health.set(animal.health)
        self.hunger = IntVar()
        self.hunger.set(animal.hunger)

        print(self.hunger.get(), self.health.get())

        self.animal = animal

        Progressbar(self.window, variable=self.hunger, maximum=animal.pr_max_hunger).pack(padx=25, pady=25)
        Button(self.window, text="Покормить", command=self.feed).pack(padx=25, pady=25)

        Progressbar(self.window, variable=self.health).pack(padx=25, pady=25)
        Button(self.window, text="Поиграть", command=self.play).pack(padx=25, pady=25)

    def tick(self):
        self.health.set(self.animal.health)
        self.hunger.set(self.animal.hunger)


    def feed(self):
        print("feeding")
        self.animal.feed()


    def play(self):
        self.animal.play()

    def close(self):
        self.window.destroy()


if __name__ == "__main__":
    game = Game()
    game.start(1)
    AnimalWindow(game.farm.animals[0])
    mainloop()
