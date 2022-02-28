from cmath import exp
from tkinter import *
from datetime import datetime

w = Tk()
w.geometry(*1280x720)
w.minsize(750,200)
w.title("Digital Clock")

f1 = Frame(w, width = 750, height = 200, bg = "#0e10113")
f1.place(x = 0, y = 0)
f1.pack(expand = True)


w.mainloop()

