from tkinter import *
from tkinter import ttk
from random import randint
from datetime import datetime as dt

ANCHOR_PLACES = ('n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw')
TIME_TO_RUN = 15    # время (сек), в течение которого кнопка убегает от мыши

def get_mouse_coord(event):
    global mouse_y, mouse_x
    mouse_x = event.x
    mouse_y = event.y
    # label.config(text=f'x={mouse_x}, y={mouse_y}')



def entered(event):
    global btn_state, start_time
    if btn_state == 0:   # 1-й раз дотронулись до кнопки - начинаем отсчёт времени!
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
    mouse_x = 0     # Координаты мыши
    mouse_y = 0

    start_time = 0  # Объявление глобальной переменной, обозначающей время начала "ловли" кнопки юзером
    btn_state = 0     # предполагаем три состояния кнопки: 0 - не начала убегать, 1 - убегает и 2 - остановилась


    root = Tk()

    root.title("Joke & Smoke")
    root.geometry("300x250+800+400")

    btn = Button(text = 'Нажми меня!', command=button_click)
    btn.pack(expand=1)
    btn.bind('<Enter>', entered)

    img = PhotoImage(file='smile.png')
    label = Label(text='С первым апреля!', font=("Times New Roman", 14), image=img, compound="bottom")

    root.bind('<Motion>', get_mouse_coord)

    mainloop()



