from tkinter import *
from random import randint
from copy import deepcopy

class Joke:

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

        # self.root.bind('<Motion>', self.get_mouse_coord)

        self.img = PhotoImage(file='smile.png')
        self.label = Label(text='С первым апреля!', font=("Times New Roman", 14), image=self.img, compound="bottom")

        self.btn_no_home = None
        self.in_place = True

        mainloop()


    def entered(self, event):
        if self.btn_no_home == None:  # Определим границы начального положения кнопки "Нет"
            self.btn_no_home = (self.btn_no.winfo_x(),
                                self.btn_no.winfo_y(),
                                self.btn_no.winfo_x() + self.btn_no.winfo_width(),
                                self.btn_no.winfo_y()  + self.btn_no.winfo_height())
        if self.in_place:
            self.button_jump(event, self.btn_no, self.btn_yes)
        else:
            self.btn_no.place(x=self.btn_no_home[0], y=self.btn_no_home[1])
        self.in_place = not self.in_place


    def get_new_coords(self, btn):
        return (randint(0, self.root.winfo_width() - btn.winfo_width() - 1),
                randint(0, self.root.winfo_height() - btn.winfo_height() - 1))

    def button_jump(self, event, btn:Button, btn1:Button):
        btn_new = self.get_new_coords(btn)
        while (btn_new[0] <= btn1.winfo_x() + btn1.winfo_width() and  btn_new[0] + btn.winfo_width() >= btn1.winfo_x()
                and btn_new[1] <= btn1.winfo_y() + btn1.winfo_height() and  btn_new[1] + btn.winfo_height() >= btn1.winfo_y()):
            btn_new = self.get_new_coords(btn)
        btn.place(x=btn_new[0], y=btn_new[1])

    def button_click(self):

        self.label.pack(expand=1)


if __name__ == '__main__':
    joke = Joke()





