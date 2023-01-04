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

            btn = Button(self.window, image=image_record[animal.state], width=100, height=100,
                         command=lambda a=self.farm.animals[i]: self.__show_window_for(a))
            btn.grid(row=i // 5, column=i % 5)

            self.__animal_btns.append(btn)

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def __show_window_for(self, animal):
        self.children.append(AnimalWindow(self.window, animal))

    def close(self):
        self.window.destroy()
        if self.on_close:
            self.on_close()

    def tick(self):
        # TODO: пройтись по всем номерам животных (self.animals),
        #  для каждого номера в кнопку по тем же номером (self.__btns) задать изображение под тем же номером (self.__images)
        #  с сотоянием этого животного (animal.state)

        for child in self.children:
            child.tick()


if __name__ == "__main__":
    game = Game()
    game.start(10)

    window = FarmWindow(game.farm)
    mainloop()
