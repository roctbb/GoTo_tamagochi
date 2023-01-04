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

        self.mood = IntVar()
        self.mood.set(animal.mood)

        print("Голод -", self.hunger.get(), ",", "Здоровье -", self.health.get(), ",", "Настроение -",self.mood.get())

        self.animal = animal

        Progressbar(self.window, variable=self.hunger, maximum=animal.pr_max_hunger).pack(padx=100, pady=25)
        Button(self.window, text="Покормить", command=self.feed).pack(padx=25, pady=25)

        Progressbar(self.window, variable=self.health, maximum=animal.pr_max_health).pack(padx=100, pady=25)
        Button(self.window, text="Помыть", command=self.wash).pack(padx=25, pady=25)

        Progressbar(self.window, variable=self.mood, maximum=animal.pr_max_mood).pack(padx=100, pady=25)
        Button(self.window, text="Играть", command=self.mood).pack(padx=25, pady=25)


    def tick(self):
        self.health.set(self.animal.health)
        self.hunger.set(self.animal.hunger)
        self.mood.set(self.animal.mood)


    def feed(self):
        print("feeding")
        self.animal.feed()


    def wash(self):
        print("washing")
        self.animal.wash()


    def play(self):
        print("playing")
        self.animal.play()


    def close(self):
        self.window.destroy()


if __name__ == "__main__":
    game = Game()
    game.start(1)
    AnimalWindow(game.farm.animals[0])
    mainloop()
