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

        # Create convert and clear buttons. When clicked, the convert and clear functions are called
        btnConvertedAmount = Button(window, text = "Convert", font = "Helvetica 12 bold", bg = "blue", fg = "white", command = self.convert).grid(row = 4, column = 1, sticky = E)
        btnDeleteAll = Button(window, text = "Clear", font = "Helvetica 12 bold", bg = "red", fg = "white", command = self.clear).grid(row = 4, column = 6, padx = 25, pady = 25, sticky = E)

        window.mainloop() # Runs the application program

        # Function to do the conversion. Stores inputs and performs conversion
        def convert(self):
            amount = float(self.conversionRate.get())
            convertedAmount = float(self.amountToConvert.get()) * amount
            self.convertedAmount.set(format(convertedAmount, '10.2f'))
        
        # Function to clear all the inputs
        def clear(self):
            self.amountToConvert.set("")
            self.conversionRate.set("")
            self.convertedAmount.set("")