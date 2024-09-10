from tkinter import *
from tkinter import ttk
from random import randint

ANCHOR_PLACES = ('n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw')


def get_mouse_coord(event):
    mouse_x = event.x
    mouse_y = event.y
    # label.config(text=f'x={mouse_x}, y={mouse_y}')


def entered(event):
    x_new = randint(0, root.winfo_width() - btn.winfo_width() - 1)
    y_new = randint(0, root.winfo_height() - btn.winfo_height() - 1)
    while x_new <= mouse_x <= x_new + btn.winfo_width() and y_new <= mouse_y <= y_new + btn.winfo_height():
        x_new = randint(0, root.winfo_width()-btn.winfo_width() - 1)
        y_new = randint(0, root.winfo_height()-btn.winfo_height() - 1)
    btn.place(x=x_new, y=y_new)



if __name__ == '__main__':
    mouse_x = 0
    mouse_y = 0
    root = Tk()

    root.title("Joke & Smoke")
    root.geometry("300x250+800+400")

    btn = Button(text = 'Нажми меня!')
    btn.pack(expand=1)
    btn.bind('<Enter>', entered)

    # label = Label()
    # label.pack(expand=1)


    root.bind('<Motion>', get_mouse_coord)


    mainloop()



