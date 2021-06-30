from tkinter import *

width, height = 700, 600
largeur, hauteur = 7, 6
taille_cellule, marge_x, marge_y = 90, 35, 7


def coo(x, y):
    x_pixel = marge_x + x * taille_cellule
    y_pixel = marge_y + y * taille_cellule
    return x_pixel, y_pixel


def creer_grille():
    x_min, y_min = 0, 0
    x_max, y_max = largeur, hauteur
    # lignes horizontales
    for y in range(hauteur + 1):
        sheet.create_line(coo(x_min, y), coo(x_max, y), fill="white", width=3)
    # lignes verticales
    for x in range(largeur + 1):
        sheet.create_line(coo(x, y_min), coo(x, y_max), fill="white", width=3)


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    return x


def add_pion():
    sheet.create_oval(coo(0, 5), coo(1, 6), fill="red")


def add_pion2():
    sheet.create_oval(coo(1, 4), coo(2, 5), fill="red")
    sheet.create_oval(coo(1, 5), coo(2, 6), fill="red")


def add_pion3():
    sheet.create_oval(coo(2, 5), coo(3, 6), fill="yellow")


def add_pion4():
    sheet.create_oval(coo(3, 5), coo(4, 6), fill="yellow")
    sheet.create_oval(coo(3, 4), coo(4, 5), fill="red")
    sheet.create_oval(coo(3, 3), coo(4, 4), fill="yellow")


def add_pion5():
    sheet.create_oval(coo(4, 5), coo(5, 6), fill="red")
    sheet.create_oval(coo(4, 4), coo(5, 5), fill="yellow")
    sheet.create_oval(coo(4, 3), coo(5, 4), fill="red")


def add_pion6():
    sheet.create_oval(coo(5, 5), coo(6, 6), fill="yellow")
    sheet.create_oval(coo(5, 4), coo(6, 5), fill="yellow")
    sheet.create_oval(coo(5, 3), coo(6, 4), fill="yellow")
    sheet.create_oval(coo(5, 2), coo(6, 3), fill="red")


def add_pion7():
    sheet.create_oval(coo(6, 5), coo(7, 6), fill="yellow")
    sheet.create_oval(coo(6, 4), coo(7, 5), fill="red")
    sheet.create_oval(coo(6, 3), coo(7, 4), fill="yellow")
    sheet.create_oval(coo(6, 2), coo(7, 3), fill="red")
    sheet.create_oval(coo(6, 1), coo(7, 2), fill="red")


def create_line():
    sheet.create_line(coo(3.5, 4.5), coo(6.5, 1.5), fill="black", width=7)


if __name__ == "__main__":
    window = Tk()
    window.title("Puissance 2+2")
    window.minsize(width, height + 50)
    window.maxsize(width, height + 50)
    window.config(bg="navy blue")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    # window.bind('<Motion>', motion)

    sheet = Canvas(window, width=width, height=height - 50, bg="navy blue", highlightthickness=0)
    under_sheet = Frame(window, width=width-50, height=50, bg="light grey", highlightthickness=0)
    under_sheet.grid(row=1, column=0)
    sheet.grid(row=0, column=0)

    btn_quit = Button(window, text='Quit', bg="red", fg="white", command=window.destroy)
    btn_quit.grid(padx=10, pady=10, sticky='se')
    btn_check = Button(window, text='Check', bg="green", fg="white", command=create_line)
    btn_check.grid(row=2, column=0, padx=10, pady=10, sticky='sw')

    bottomframe = Frame(under_sheet)
    bottomframe.pack(side=BOTTOM)

    col1button = Button(under_sheet, text="       1       ", fg="black", command=add_pion)
    col1button.pack(side=LEFT)
    col2button = Button(under_sheet, text="       2       ", fg="black", command=add_pion2)
    col2button.pack(side=LEFT)
    col3button = Button(under_sheet, text="       3       ", fg="black", command=add_pion3)
    col3button.pack(side=LEFT)
    col4button = Button(under_sheet, text="       4       ", fg="black", command=add_pion4)
    col4button.pack(side=LEFT)
    col5button = Button(under_sheet, text="       5       ", fg="black", command=add_pion5)
    col5button.pack(side=LEFT)
    col6button = Button(under_sheet, text="       6       ", fg="black", command=add_pion6)
    col6button.pack(side=LEFT)
    col7button = Button(under_sheet, text="       7       ", fg="black", command=add_pion7)
    col7button.pack(side=LEFT)

    creer_grille()
    window.mainloop()