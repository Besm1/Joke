from tkinter import *
from random import randint
from datetime import datetime as dt

class Joke:

    # TIME_TO_RUN = 15    # время (сек), в течение которого кнопка убегает от мыши
    #
    # start_time = 0  # Объявление атрибута класса, обозначающего время начала "ловли" кнопки юзером
    # btn_state = 0     # предполагаем три состояния кнопки: 0 - не начала убегать, 1 - убегает и 2 - остановилась

    root = None

    def __init__(self):
        self.root = Tk()
        self.root.title("Joke & Smoke")
        self.root.geometry("300x250+800+400")

        self.btn_yes = Button(text = 'Да', command=self.button_click, height=1, width=6, padx=5)
        self.btn_yes.place(x=75, y=112)

        self.btn_no = Button(text='Нет', height=1, width=6, padx=5)
        self.btn_no.place(x=165, y=112)
        self.btn_no.bind('<Enter>', self.entered)

        self.root.bind('<Motion>', self.get_mouse_coord)

        self.img = PhotoImage(file='smile.png')
        self.label = Label(text='С первым апреля!', font=("Times New Roman", 14), image=self.img, compound="bottom")

        self.btn_no_home = None

        mainloop()
        print('start')

    def get_mouse_coord(self, event):
        self.mouse_at = (event.x, event.y)



    def entered(self, event):
        if self.btn_no_home == None:  # Определим границы начального положения кнопки "Нет"
            self.btn_no_home = (self.btn_no.winfo_x(),
                                self.btn_no.winfo_y(),
                                self.btn_no.winfo_x() + self.btn_no.winfo_width(),
                                self.btn_no.winfo_y()  + self.btn_no.winfo_width())
        self.button_jump(event, self.btn_no, self.btn_yes)


    def get_new_coords(self, btn):
        return (randint(0, self.root.winfo_width() - btn.winfo_width() - 1),
                randint(0, self.root.winfo_height() - btn.winfo_height() - 1))

    def button_jump(self, event, btn:Button, btn1:Button):
        mouse_x = btn.winfo_x() + event.x
        mouse_y = btn.winfo_y() + event.y
        x_new , y_new = self.get_new_coords(btn)
        while ((x_new <= mouse_x <= x_new + btn.winfo_width() and y_new <= mouse_y <= y_new + btn.winfo_height()) or
                (x_new <= btn1.winfo_x() + btn1.winfo_width() and  x_new + btn.winfo_width() >= btn1.winfo_x()
                and y_new <= btn1.winfo_y() + btn1.winfo_height() and  y_new + btn.winfo_height() >= btn1.winfo_y())):
            x_new, y_new = self.get_new_coords(btn)
        btn.place(x=x_new, y=y_new)

    def button_click(self):

        self.label.pack(expand=1)

if __name__ == '__main__':
    joke = Joke()





