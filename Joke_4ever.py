from tkinter import *
from random import randint


class Joke_From_HR:

    def __init__(self):
        self.root = Tk()
        self.root.title("Опрос отдела кадров")
        self.root.geometry("300x250+800+600")

        self.btn_yes = Button(text = 'Да', command=self.button_click, height=1, width=6, padx=5)
        self.btn_yes.place(x=75, y=112)

        self.btn_no = Button(text='Нет', height=1, width=6, padx=5)
        self.btn_no.place(x=165, y=112)
        self.btn_no.bind('<Enter>', self.entered)

        self.question = Label(text='Вы довольны\nуровнем своей зарплаты?', font=("Times New Roman", 14),
                               foreground='blue')
        self.question.pack(side=TOP)

        self.conclusion = Label(text='Спасибо за участие в опросе!\nВаш честный ответ будет\nпередан в отдел кадров.'
                                , font=("Times New Roman", 16, 'bold'), foreground='red')

        self.btn_no_home = None # Здесь впоследствии сохраним "домашние" координаты кнопки "Нет"
        self.btn_no_at_home = True    # Переключатель


        mainloop()


    def entered(self, event):
        if self.btn_no_home == None:  # Определим границы начального положения кнопки "Нет"
            self.btn_no_home = (self.btn_no.winfo_x(), # левый верхний угол
                                self.btn_no.winfo_y(),
                                                        # правый нижний угол:
                                self.btn_no.winfo_x() + self.btn_no.winfo_width(),
                                self.btn_no.winfo_y()  + self.btn_no.winfo_height())
        if self.btn_no_at_home:   # Если кнопка "Нет" на своём месте, то переместим её
            self.button_jump(event, self.btn_no)
        else:   # Иначе восстановим на своё место.
            self.btn_no.place(x=self.btn_no_home[0], y=self.btn_no_home[1])

        self.btn_no_at_home = not self.btn_no_at_home   # Переключим индикатор


    def get_new_coords(self, btn):
            # Определим случайные новые координаты кнопки btn
        return (randint(0, self.root.winfo_width() - btn.winfo_width() - 1),
                randint(0, self.root.winfo_height() - btn.winfo_height() - 1))


    def button_jump(self, event, btn:Button):
        btn_new = self.get_new_coords(btn)
        btn_new_coords = (btn_new[0],btn_new[1]  # верхний левый угол нового положения,
                          , btn_new[0] + self.btn_no.winfo_width()  # ниже - нижний правый угол
                          , btn_new[1] +self.btn_no.winfo_height())

        # пока есть пересечение кнопки в новом положении с любым их виджетов на экране, ищем новые координаты
        while any(intersection(btn_new_coords, w_) for w_ in (self.btn_yes, self.question, self.btn_no_home))  :
            btn_new = self.get_new_coords(btn)
            btn_new_coords = (btn_new[0],btn_new[1], btn_new[0] + self.btn_no.winfo_width()
                                , btn_new[1] +self.btn_no.winfo_height())

        btn.place(x=btn_new[0], y=btn_new[1])

    def button_click(self):
        self.btn_no.destroy()   # Нажали на "Да"
        self.conclusion.pack(side=BOTTOM)

def intersection(coords1, coords2) -> bool:
    """
    Определяет наличие пересечения двух виджетов по их координатам
    :param coords1: тип - либо итерируемый, длиной 4 - координаты левой верхней и правой нижней точек виджета
                          либо tkinter.Widget
    :param coords2: - то же.
    :return: True - есть пересечение, False - нет
    """
    if coords1.__class__.__bases__[0].__name__ == 'Widget':
        coords1 = w_coords(coords1)
    if coords2.__class__.__bases__[0].__name__ == 'Widget':
        coords2 = w_coords(coords2)
    if (isinstance(coords1, (tuple, list, set)) and len(coords1) == 4
            and isinstance(coords2, (tuple, list, set)) and len(coords2) == 4):
        ret = (coords1[0] <= coords2[2] and coords1[2] >= coords2[0]
                and coords1[1] <= coords2[3] and coords1[3] >= coords2[1])
        print(f'ret: {ret}')
        return ret
    else:
        return True

def w_coords(w:Widget):
    """
    Преобразует объект типа tkinter.Widget в кортеж длиной 4 - координаты его левой верхней и правой нижней точек
    """
    return w.winfo_x(), w.winfo_y(), w.winfo_x() + w.winfo_width(), w.winfo_y() + w.winfo_height()

if __name__ == '__main__':
    joke = Joke_From_HR()

