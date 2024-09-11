from tkinter import *
from tkinter import ttk
from random import randint
from datetime import datetime as dt

class Joke:

    TIME_TO_RUN = 15    # время (сек), в течение которого кнопка убегает от мыши
    mouse_x = 0     # Координаты мыши
    mouse_y = 0

    start_time = 0  # Объявление глобальной переменной, обозначающей время начала "ловли" кнопки юзером
    btn_state = 0     # предполагаем три состояния кнопки: 0 - не начала убегать, 1 - убегает и 2 - остановилась

    root = None

    def __init__(self):
        self.root = Tk()
        self.root.title("Joke & Smoke")
        self.root.geometry("300x250+800+400")

        self.btn = Button(text = 'Нажми меня!', command=button_click)
        self.btn.pack(expand=1)
        self.btn.bind('<Enter>', self.entered)

        img = PhotoImage(file='smile.png')
        self.label = Label(text='С первым апреля!', font=("Times New Roman", 14), image=img, compound="bottom")

        self.root.bind('<Motion>', self.get_mouse_coord)

        mainloop()

    def set_mouse_coord(self):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def get_mouse_coord(event):
        self.set_mouse_coord

    def entered(event, self):
        if self.btn_state == 0:   # 1-й раз дотронулись до кнопки - начинаем отсчёт времени!
            btn_state = 1   # начинаем убегать!
            start_time = dt.now()
            button_jump()
        elif btn_state == 1:  # продолжаем убегать...
            if (dt.now() - start_time).seconds > TIME_TO_RUN:  #start_time > TIME_TO_RUN:
                btn_state = 2   # Кончили убегать
            else:
                button_jump()

    def get_new_coords(root, btn):
        return randint(0, root.winfo_width() - btn.winfo_width() - 1), randint(0, root.winfo_height() - btn.winfo_height() - 1)

    def button_jump():
        global mouse_y, mouse_x, root, btn
        x_new , y_new = get_new_coords(root, btn)
        while x_new <= mouse_x <= x_new + btn.winfo_width() and y_new <= mouse_y <= y_new + btn.winfo_height():
            x_new, y_new = get_new_coords(root, btn)
        btn.place(x=x_new, y=y_new)

    def button_click():
        global label, btn
        btn.destroy()
        label.pack(expand=1)

if __name__ == '__main__':




