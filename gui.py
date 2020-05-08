# GUI for Degiro max share purchase calculator.
# Created By: Rory Williams Doyle.

from tkinter import *


class Window(Frame):
    """
    A generic class for creating windows.
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


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
