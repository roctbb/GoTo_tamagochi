from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from domain.animal import Animal
from domain.game import Game

number = 0
class AnimalWindow:
    def __init__(self, parent, animal):
        self.window = Toplevel(parent)
        self.window.title("Питомец")

        self.animal = animal

        self.health_var = IntVar()
        self.hunger_var = IntVar()
        self.mood_var = IntVar()

        self.update()

        print("Голод -", self.hunger_var.get(), ",", "Здоровье -", self.health_var.get(), ",", "Настроение -",
              self.mood_var.get())

        Progressbar(self.window, variable=self.hunger_var, maximum=animal.pr_max_hunger).grid(row=1, column=0)
        Button(self.window, text="Покормить", command=self.feed).grid(row=1, column=0)

        Progressbar(self.window, variable=self.health_var, maximum=animal.pr_max_health).grid(row=1, column=0)
        Button(self.window, text="Помыть", command=self.wash).grid(row=1, column=0)

        Progressbar(self.window, variable=self.mood_var, maximum=animal.pr_max_mood).grid(row=1, column=0)
        Button(self.window, text="Играть", command=self.play).grid(row=1, column=0)


    def tick(self):
        self.update()


    def update(self):
        self.health_var.set(self.animal.health)
        self.hunger_var.set(self.animal.hunger)
        self.mood_var.set(self.animal.mood)


    def feed(self):
        print("feeding")
        self.animal.feed()
        self.update()


    def wash(self):
        print("washing")
        self.animal.wash()
        self.update()


    def play(self):
        print("playing")
        self.animal.play()
        self.update()


    def close(self):
        self.window.destroy()


if __name__ == "__main__":
    game = Game()
    game.start(1)
    AnimalWindow(game.farm.animals[0])
    mainloop()
