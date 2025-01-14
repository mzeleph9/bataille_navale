from cProfile import label
from tkinter import *

fenetre = Tk()

fenetre.title("Bataille Navale")
fenetre.minsize(1000, 600)
fenetre.maxsize(1000,600)
fenetre.iconbitmap("img/logo.ico")

titre = Label(fenetre,text="Bataille Navale",fg="black",font=("Courrier",60))
titre.pack()



fenetre.mainloop()