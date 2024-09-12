from tkinter import *
from random import randint
from datetime import datetime as dt

class Joke:

    TIME_TO_RUN = 15    # время (сек), в течение которого кнопка убегает от мыши

    start_time = 0  # Объявление атрибута класса, обозначающего время начала "ловли" кнопки юзером
    btn_state = 0     # предполагаем три состояния кнопки: 0 - не начала убегать, 1 - убегает и 2 - остановилась

    root = None

    def __init__(self):
        self.root = Tk()
        self.root.title("Joke & Smoke")
        self.root.geometry("300x250+800+400")

        self.btn = Button(text = 'Нажми меня!', command=self.button_click)
        self.btn.pack(expand=1)
        self.btn.bind('<Enter>', self.entered)

        self.img = PhotoImage(file='smile.png')
        self.label = Label(text='С первым апреля!', font=("Times New Roman", 14), image=self.img, compound="bottom")

    def start(self):
        mainloop()

    def entered(self, event):
        if self.btn_state == 0:   # 1-й раз дотронулись до кнопки - начинаем отсчёт времени!
            self.btn_state = 1   # начинаем убегать!
            self.start_time = dt.now()
            self.button_jump(event.x, event.y)
        elif self.btn_state == 1:  # продолжаем убегать...
            if (dt.now() - self.start_time).seconds > self.TIME_TO_RUN:  #start_time > TIME_TO_RUN:
                self.btn_state = 2   # Кончили убегать
            else:
                self.button_jump( event.x, event.y)

    def get_new_coords(self):
        return (randint(0, self.root.winfo_width() - self.btn.winfo_width() - 1),
                randint(0, self.root.winfo_height() - self.btn.winfo_height() - 1))

    def button_jump(self, event_x, event_y):
        # global mouse_y, mouse_x, root, btn
        mouse_x = self.btn.winfo_x() + event_x
        mouse_y = self.btn.winfo_y() + event_y
        x_new , y_new = self.get_new_coords()
        while x_new <= mouse_x <= x_new + self.btn.winfo_width() and y_new <= mouse_y <= y_new + self.btn.winfo_height():
            x_new, y_new = self.get_new_coords()
        self.btn.place(x=x_new, y=y_new)

    def button_click(self):
        # global label, btn
        self.btn.destroy()
        self.label.pack(expand=1)

if __name__ == '__main__':
    joke = Joke()
    joke.start()




