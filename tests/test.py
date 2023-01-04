from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox


# Функция для уменьшения жизни каждую секунду
def check_life():
    # узнаем, какая сейчас жизнь из прогресс бара
    current_life = life.get()

    # уменьшаем значение на прогрессбаре
    life.set(current_life - 1)

    # если жизни мало - закрываем приложение
    if current_life <= 1:
        messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
        quit()
    # иначе запускаем функция еще через секунду
    else:
        window.after(1000, check_life)


# функция для кормления
def feed():
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

# включаем таймер для уменьшения жизни через секунду
window.after(1000, check_life)

mainloop()
