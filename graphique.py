from Puissance_4.init import *
from tkinter import *
from tkinter import font as tkFont
import pyautogui
import time


width, height = 700, 600
largeur, hauteur = 7, 6
taille_cellule, marge_x, marge_y = 90, 35, 7
sec = 0
global ok
ok = False


def timerupdate2(sec=0):
    sec = sec + 1
    label.configure(text=sec)
    window.after(1000, timerupdate2)


class App():
    def __init__(self):
        self.window = Tk()
        self.root = Frame(self.window, height=200, width=200)
        self.root.pack()
        self.root.pack_propagate(0)
        self.window.title('Timer')
        self.label = Label(text="")
        self.label.pack()
        self.sec = 0
        self.timerupdate()
        self.root.mainloop()

    def timerupdate(self):
        self.sec = self.sec + 1
        self.label.configure(text=self.sec)
        self.root.after(1000, self.timerupdate)


class P4graph:
    def __init__(self, row=0, col=0, j1='', j2=''):
        self.row = row
        self.col = col
        self.j1 = j1
        self.j2 = j2
        self.user_name = None
        self.counterJ1 = 21
        self.counterJ2 = 21
        self.game_status = {"Egalité": 0, "Victoire J1": 0, "Victoire J2": 0}
        self.col_used = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}


def coo(x, y):
    x_pixel = marge_x + x * taille_cellule
    y_pixel = marge_y + y * taille_cellule
    return x_pixel, y_pixel


def creer_grille():
    x_min, y_min = 0, 0
    x_max, y_max = largeur, hauteur
    # lignes horizontales
    for y in range(hauteur + 1):
        sheet.create_line(coo(x_min, y), coo(x_max, y), fill="white")
    # lignes verticales
    for x in range(largeur + 1):
        sheet.create_line(coo(x, y_min), coo(x, y_max), fill="white")


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    return x


def add_rond():
    img = PhotoImage(file="images/red.png")
    sheet.create_image(coo(3 + 0.5, 3 + 0.5), anchor=CENTER, image=img)


def fct():
    ok = True
    return ok

if __name__ == "__main__":
    #app = App()

    window = Tk()
    window.title("Puissance 2+2")
    window.minsize(width, height+50)
    window.maxsize(width, height+50)
    window.config(bg="navy blue")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    #window.bind('<Motion>', motion)

    sheet = Canvas(window, width=width, height=height-50, bg="navy blue", highlightthickness=0)
    under_sheet = Frame(window, width=width, height=50, bg="light grey", highlightthickness=0)
    under_sheet.grid(row=1, column=0)
    sheet.grid(row=0, column=0)

    #root = Tk()
    #frame = Frame(root)
    #frame.pack()

    bottomframe = Frame(under_sheet)
    bottomframe.pack(side=BOTTOM)

    col1button = Button(under_sheet, text=" 1 ", fg="red", command=window.destroy)
    col1button.pack(side=LEFT)

    col2button = Button(under_sheet, text=" 2 ", fg="red")
    col2button.pack(side=LEFT)

    col3button = Button(under_sheet, text=" 3 ", fg="red")
    col3button.pack(side=LEFT)

    col4button = Button(under_sheet, text=" 4 ", fg="red")
    col4button.pack(side=LEFT)

    col5button = Button(under_sheet, text=" 5 ", fg="red")
    col5button.pack(side=LEFT)

    col6button = Button(under_sheet, text=" 6 ", fg="red")
    col6button.pack(side=LEFT)

    col7button = Button(under_sheet, text=" 73 ", fg="red", command=fct())
    col7button.pack(side=LEFT)

    #btn_quit = Button(window, text='Quit', bg='white', command=window.destroy)
    #btn_quit.grid(row=1, column=1, padx=10, pady=10)

    creer_grille()
    sheet.create_text(coo(5 + 0.5, 5 + 0.5), text=2, fill="white")
    sheet.create_text(coo(0 + 0.5, 2 + 0.5), text=1, fill="white")
    sheet.create_text(coo(6 + 0.5, 2 + 0.5), text=1, fill="white")

    if ok == True:
        img = PhotoImage(file="images/red.png")
        sheet.create_image(coo(3 + 0.5, 3 + 0.5), anchor=CENTER, image=img)

    window.mainloop()