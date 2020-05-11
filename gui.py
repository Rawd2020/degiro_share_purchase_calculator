# GUI for Degiro max share purchase calculator.
# Created By: Rory Williams Doyle.

from tkinter import *
from maxShares import maxShares


class Window(Frame):
    """
    Our window content class.
    """
    def __init__(self, master=None):
        """
        Main function that spawns our GUI window + content.
        """

        # Window setup.
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Key bindings
        self.master.bind('<Return>', self.calculateMaxPurchasableUnits)  # Connect submit func to return key.
        
        # Main description.
        text = Label(self, text="Please enter the share price & funds available to calculate the\n maximum purchasable shares.")
        text.place(x=50,y=10)

        # Funds available text box.
        text = Label(self, text="Funds available (€):")
        text.place(x=10,y=77)
        self.funds = Entry(self, show=None, font=('Arial', 14))  
        self.funds.place(x=150,y=75)

        # Unit Price text box.
        text = Label(self, text="Cost per investment unit (€):")
        text.place(x=10,y=112)
        self.price = Entry(self, show=None, font=('Arial', 14))  
        self.price.place(x=210,y=110)

        # Fixed fee text box.
        text = Label(self, text="Fixed cost of investment (€):")
        text.place(x=10,y=147)
        self.fixedFee = Entry(self, show=None, font=('Arial', 14))  
        self.fixedFee.place(x=210,y=145)

        # Percentage cost text box.
        text = Label(self, text="Percentage fee of investment (0 - 1):")
        text.place(x=10,y=182)
        self.varFee = Entry(self, show=None, font=('Arial', 14))  
        self.varFee.place(x=260,y=180)

        # Submission button.
        submitButton = Button(self, text="Calculate", command=self.calculateMaxPurchasableUnits)
        submitButton.place(x=200,y=215)

        # Result text box.
        text = Label(self, text="Result:", font=('Arial', 14))
        text.place(x=10,y=300)
        self.result = Label(text="?", font=('Arial', 14))
        self.result.place(x=80,y=301)

    def calculateMaxPurchasableUnits(self, event=None):
        """
        Reads the figures from our four text fields and calculates
        the max number of investment units purchasable.
        """
        self.result.configure(text=maxShares(self.funds.get(), self.price.get(), self.fixedFee.get(), self.varFee.get()))
        

def main():
    """
    Main function for the GUI code.
    """
    # Creates our main window.
    root = Tk()
    app = Window(root)

    root.wm_title("Degiro Share Purchase Calculator")  # Sets the main window title bar.
    root.geometry("500x500")  # Sets window size.
    root.mainloop()  # Kick of the GUI main loop.


if __name__ == "__main__":
    main()
