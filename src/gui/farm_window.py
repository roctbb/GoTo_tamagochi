from domain.animal import Animal
from gui.animal_window import AnimalWindow
from tkinter import *
from config import *
from domain.game import Game
from domain.common import asset_path
from PIL import Image, ImageTk


class FarmWindow:
    def __init__(self, parent, farm):
        self.farm = farm
        self.window = Toplevel(parent)
        self.window.title('Tamagotchi')
        self.children = []
        self.__images = []
        self.on_close = None



        for i in range(len(self.farm.animals)):
            image_type = self.farm.animals[i].image
            image_path = asset_path(IMAGES[image_type]["normal"])
            img = Image.open(image_path).resize((100,100))
            img_photo = ImageTk.PhotoImage(img)
            self.__images.append(img_photo)

            btn = []
            Button(self.window, image=img_photo, width=100, height=100, command=lambda: self.__show_window_for(self.farm.animals[i]) +).grid(
                row=i // 5, column=i % 5)

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def __show_window_for(self, animal):
        self.children.append(AnimalWindow(self.window, animal))

    def close(self):
        self.window.destroy()
        if self.on_close:
            self.on_close()

    def tick(self):
        if Animal.is_bad() == True:
            image_path = asset_path(IMAGES[Animal.image_type]["bad"])

        for child in self.children:
            child.tick()


if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
