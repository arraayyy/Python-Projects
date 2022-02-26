from cProfile import label
from cgitb import text
from curses import window
from tkinter import * 

class currencyConverter: # Create class
    def __init__(self) -> None: # Special method in Python class
        window = Tk() # Create Application window
        window.title("Currency Converter") # Add title to the application window 
        window.configure(bg = "yellow") # Add background color to the application window

        # Adding label widgets to application window
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to Convert").grid(row = 1, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Conversion Rate").grid(row = 2, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Converted Amount").grid(row = 3, column = 1, sticky = W)
        
        # Create objects and add entry functions
        self.amountToConvert = StringVar()
        Entry(window, textvariable = self.amountToConvert, bg = "white", justify = RIGHT).grid(row = 1, column = 2)
        self.conversionRate = StringVar()
        Entry(window, textvariable = self.conversionRate, bg = "white", justify = RIGHT).grid(row = 2, column = 2)
        self.convertedAmount = StringVar()
        lblConvertedAmount = Label(window, textvariable = self.convertedAmount, bg = "yellow", font = "Helvetica 12 bold").gird(row = 3, column = 2, sticky = E)
