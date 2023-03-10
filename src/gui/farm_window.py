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
        self.last_child = None

        self.__images = []
        self.__animal_btns = []

        self.on_close = None

        for i in range(len(self.farm.animals)):
            animal = self.farm.animals[i]
            image_type = animal.image

            image_record = {}

            for state in ["normal", "bad"]:
                image_path = asset_path(IMAGES[image_type][state])
                img = Image.open(image_path).resize((100, 100))
                img_photo = ImageTk.PhotoImage(img)
                image_record[state] = img_photo

            self.__images.append(image_record)

            Label(self.window, text=animal.name).grid(row=2 * (i // 5), column=i % 5)

            btn = Button(self.window, image=image_record[animal.state], width=100, height=100,
                         command=lambda a=animal: self.__show_window_for(a))
            btn.grid(row=2 * (i // 5) + 1, column=i % 5)

            self.__animal_btns.append(btn)

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def __show_window_for(self, animal):
        if self.last_child:
            self.last_child.close()
        self.last_child = AnimalWindow(self.window, animal)

    def close(self):
        if self.last_child:
            self.last_child.close()
        self.window.destroy()
        if self.on_close:
            callback = self.on_close
            self.on_close = None
            callback()


    def tick(self):
        for i in range(len(self.farm.animals)):
            self.__animal_btns[i].configure(image=self.__images[i][self.farm.animals[i].state])

        if self.last_child:
            self.last_child.tick()


if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
