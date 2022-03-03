from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="light blue")

        Label(window, text="Annual Interest Rate", font = 'Helvetica 12 bold' ,bg="light blue").grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years", font = 'Helvetica 12 bold' ,bg="light blue").grid(row=2, column=1, sticky=W)
        Label(window, text="Loan Amount", font = 'Helvetica 12 bold' ,bg="light blue").grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment", font = 'Helvetica 12 bold' ,bg="light blue").grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment", font = 'Helvetica 12 bold' ,bg="light blue").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()    
        lblMonthlyPayment = Label(window, font='Helvetica 12 bold', bg="light blue", textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg="light blue", textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window, text="Compute Payment", bg="red", fg="white", font='Helvetica 14 bold', command= self.computePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text="Clear", bg="blue", fg="white", font='Helvetica 14 bold', command= self.delete_all).grid(row=6, column=8, sticky=E, padx=20, pady=20)
        