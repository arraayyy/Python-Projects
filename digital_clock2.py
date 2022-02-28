from cmath import exp
from time import strftime
from tkinter import *
from datetime import datetime

w = Tk()
w.geometry(*1280x720)
w.minsize(750,200)
w.title("Digital Clock")

f1 = Frame(w, width = 750, height = 200, bg = "#0e10113")
f1.place(x = 0, y = 0)
f1.pack(expand = True)

def time():
    a = strftime("%H   :   %M   :   %S")
    lbl.config(text = a)
    lbl.after(1000, time)

lbl = Label(f1, font = ('Century Gothic', 60), bg = "black", fg = "#d3d3d3")
lbl.place(x = 270, y = 35)


w.mainloop()

