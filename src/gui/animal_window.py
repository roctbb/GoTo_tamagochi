from tkinter.ttk import *
from tkinter import *
from tokenize import Name
from tkinter import *
from PIL import Image, ImageTk
from pkg_resources.extern import names

from config import IMAGES
from domain.common import asset_path
from domain.game import Game

class AnimalWindow:

    def __init__(self, parent, animal):
        self.window = Toplevel(parent)
        self.window.title("Питомец")

        self.animal = animal

        self.__images = {}
        for state in ["normal", "bad"]:
            image_path = asset_path(IMAGES[self.animal.image][state])
            img = Image.open(image_path).resize((100, 100))
            img_photo = ImageTk.PhotoImage(img)
            self.__images[state] = img_photo

        self.health_var = IntVar()
        self.hunger_var = IntVar()
        self.mood_var = IntVar()

        print("Голод -", self.hunger_var.get(), ",", "Здоровье -", self.health_var.get(), ",", "Настроение -",
              self.mood_var.get())

        Progressbar(self.window, variable=self.hunger_var, maximum=animal.pr_max_hunger).grid(row=1, column=1)
        Button(self.window, text="Кормить", command=self.feed, fg="green").grid(row=1, column=2)

        Progressbar(self.window, variable=self.health_var, maximum=animal.pr_max_health).grid(row=2, column=1)
        Button(self.window, text="Помыть", command=self.wash, fg="green").grid(row=2, column=2)

        Progressbar(self.window, variable=self.mood_var, maximum=animal.pr_max_mood).grid(row=3, column=1)
        Button(self.window, text="Играть", command=self.play, fg="green").grid(row=3, column=2)

        Label(self.window, text=animal.name, width=25, height=5).grid(row=0, column=1)
        self.__image_label = Label(self.window, image=self.__images[self.animal.state])
        self.__image_label.grid(row=1, column=0, rowspan=3)

        self.update()

    def tick(self):
        self.update()

    def update(self):
        self.__image_label.configure(image=self.__images[self.animal.state])
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
