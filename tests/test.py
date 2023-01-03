
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

def check_life():
    current_life = life.get()

    life.set(current_life - 1)

    if current_life <= 1:
        messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
        quit()
    else:
        window.after(1000, check_life)

def feed():
    # устанавливаем жизнь на максимум
    life.set(100)

def game():
    # устанавливаем жизнь на максимум
    life.set(100)


window = Tk()
window.title("Питомец")

# поскольку жизнь - числовая характеристика, вместо StringVar - IntVar
life = IntVar()
life.set(50)

# добавляем прогресс-бар
Progressbar(window, variable=life).pack(padx=25, pady=25)

# добавляем кнопку для увеличения жизни
Button(window, text="Покормить", command=feed).pack(padx=25, pady=25)

Progressbar(window, variable=life).pack(padx=25, pady=25)

# добавляем кнопку для увеличения жизни
Button(window, text="Поиграть", command=game).pack(padx=25, pady=25)

# включаем таймер для уменьшения жизни через секунду
window.after(1000, check_life)

mainloop()