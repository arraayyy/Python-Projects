from tkinter import * 

class currencyConverter: # Create class
    def __init__(self): # Special method in Python class
        window = Tk() # Create Application window
        window.title("Currency Converter") # Add title to the application window 
        window.configure(bg = "yellow") # Add background color to the application window

        # Adding label widgets to application window
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to Convert").grid(row = 1, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Conversion Rate").grid(row = 2, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Converted Amount").grid(row = 3, column = 1, sticky = W)
        
        # Create objects and add entry functions
        self.amountToConvert = StringVar()
        Entry(window, textvariable = self.amountToConvert, justify = RIGHT).grid(row = 1,column = 2)
        self.conversionRate = StringVar()
        Entry(window, textvariable = self.conversionRate, justify = RIGHT).grid(row = 2,column = 2)
        self.convertedAmount = StringVar()
        lblConvertedAmount = Label(window, font = "Helvetica 12 bold", bg = "yellow", textvariable = self.convertedAmount).grid(row = 3,column = 2,sticky = E)
        
        # Create convert and clear buttons . When clicked they will call their respective functions.
        btnConvertedAmount = Button(window, text = "Convert",font = "Helvetica 12 bold",bg = "blue",fg = "white",command = self.ConvertedAmount).grid(row = 4,column = 2,sticky = E)
        btndelete_all = Button(window, text = "Clear", font = "Helvetica 12 bold", bg = "red",fg = "white",command = self.delete_all).grid(row = 4,column = 6,padx = 25,pady = 25,sticky = E)

        window.mainloop()  # Runs the application program

        # Function to do the conversion. Stores inputs and performs conversion
    def ConvertedAmount(self):
        amount = float(self.conversionRate.get())
        convertedAmount =float(self.amounttoConvert.get()) * amount
        self.convertedAmount.set(format(convertedAmount, '10.2f'))

        # Function to clear inputs
    def delete_all(self):
        self.amounttoConvert.set("")
        self.conversionRate.set("")
        self.convertedAmount.set("")

currencyConverter()