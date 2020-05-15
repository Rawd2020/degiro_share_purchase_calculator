# GUI for Degiro max share purchase calculator.
# Created By: Rory Williams Doyle.

from tkinter import *
from maxShares import maxShares


class Window(Frame):
    """
    Our window content class.
    """
    def __init__(self, master=None, feeObject=None):
        """
        Main function that spawns our GUI window + content.
        """

        # Window setup.
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.feeObject = feeObject
        self.exchange = None
        self.fixedFees = StringVar()
        self.percentageFees = StringVar()
        self.feesPerShare = StringVar()
        self.maxFees = StringVar()
        self.transactionTax = StringVar().set("0")

        # Key bindings
        self.master.bind('<Return>', self.calculateMaxPurchasableUnits)  # Connect submit func to return key.
        
        # Main description.
        text = Label(
            self, 
            text=(
                "Prepopulated fee per share values require a conversion. See the Degiro\n"
                "fee schedual for the currency. This calculator doesn't factor\n"
                "in transaction taxes."
            )
        )
        text.place(x=10,y=10)

        # Stock Exchange Drop Down.
        def updateFees(*args):
            """
            Event listner to update fees based on the selected exchange.
            """
            self.fixedFees.set(str(self.feeObject.basicFees[self.exchange.get()]['fixedFee']))
            try:
                self.percentageFees.set(str(self.feeObject.basicFees[self.exchange.get()]['percentageFee']))
                self.feesPerShare.set("")
            except KeyError:
                self.feesPerShare.set(str(self.feeObject.basicFees[self.exchange.get()]['perShareFee']))
                self.percentageFees.set("")
            try:
                self.maxFees.set(str(self.feeObject.basicFees[self.exchange.get()]['maxFee']))
            except KeyError:
                self.maxFees.set("")

        exchanges = list(self.feeObject.basicFees.keys())
        self.exchange = StringVar(self.master)
        self.exchange.trace("w", updateFees)
        self.exchange.set(exchanges[0])
        text = Label(self, text="Select stock exchange:")
        text.place(x=10,y=70)
        self.exchangeSelector = OptionMenu(self.master, self.exchange, *exchanges)
        self.exchangeSelector.place(x=200,y=65)

        # Funds available text box.
        text = Label(self, text="Funds available:")
        text.place(x=10,y=112)
        self.funds = Entry(self, show=None, font=('Arial', 14))  
        self.funds.place(x=200,y=110)

        # Unit Price text box.
        text = Label(self, text="Cost per investment unit:")
        text.place(x=10,y=147)
        self.price = Entry(self, show=None, font=('Arial', 14))  
        self.price.place(x=200,y=145)

        # Fixed fee text box.
        text = Label(self, text="Fixed fees:")
        text.place(x=10,y=182)
        self.fixedFee = Entry(self, textvariable=self.fixedFees, show=None, font=('Arial', 14))  
        self.fixedFee.place(x=200,y=180)

        # Percentage cost text box.
        text = Label(self, text="Percentage fee (0 - 1):")
        text.place(x=10,y=217)
        self.percentageFee = Entry(self, textvariable=self.percentageFees, show=None, font=('Arial', 14))  
        self.percentageFee.place(x=200,y=215)

        # Cost per share text box.
        text = Label(self, text="Fee per share:")
        text.place(x=10,y=252)
        self.perShareFee = Entry(self, textvariable=self.feesPerShare, show=None, font=('Arial', 14))  
        self.perShareFee.place(x=200,y=250)

        # Maximum fees text box.
        text = Label(self, text="Maximum fees:")
        text.place(x=10,y=290)
        self.maxFee = Entry(self, textvariable=self.maxFees, show=None, font=('Arial', 14))  
        self.maxFee.place(x=200,y=285)

        # Submission button.
        submitButton = Button(self, text="Calculate", command=self.calculateMaxPurchasableUnits)
        submitButton.place(x=200,y=355)

        # Result text box.
        text = Label(self, text="Result:", font=('Arial', 14))
        text.place(x=10,y=419)
        self.result = Label(text="?", font=('Arial', 14))
        self.result.place(x=80,y=420)

    def calculateMaxPurchasableUnits(self, event=None):
        """
        Reads the figures from our four text fields and calculates
        the max number of investment units purchasable.
        """
        self.result.configure(
            text=maxShares(
                self.funds.get(),
                self.price.get(),
                self.fixedFee.get(),
                self.percentageFees.get(),
                self.feesPerShare.get(),
                self.maxFees.get()
            )
        )
        

def gui(feeObject=None):
    """
    Main function for the GUI code.

    :param feeObject: An optional param that is a DegiroFees object instance.
    """
    # Creates our main window.
    root = Tk()
    app = Window(root, feeObject)

    root.wm_title("Degiro Share Purchase Calculator")  # Sets the main window title bar.
    root.geometry("500x500")  # Sets window size.
    root.mainloop()  # Kick of the GUI main loop.


if __name__ == "__main__":
    gui()
