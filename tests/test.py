from tkinter import *
from PIL import Image, ImageTk

img1 = ImageTk.PhotoImage(Image.open("face1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("face2.jpg"))

image_label = Label(self.window, image=img1)
image_label.pack()

# когда хотим поменять картинку - вызываем configure
image_label.configure(image=img2)