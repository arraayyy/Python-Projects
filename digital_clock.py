# from cgitb import text
from tkinter import *
from time import strftime # function within the time module that retrieves you computer's time

root = Tk() # Create tkinter window
root.title("Digital Clock") # Title
 
# Function used to display time on the label
def time(): 
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling label widget
lbl = Label(root, font = ("arial", 160, "bold"), bg = "black", fg = "white")

# Pack method in tkinter packs widget into rows or columns
lbl.pack(anchor = "center", fill = "both", expand = 1)

time() # Time functions is called

mainloop() # Runs the application program