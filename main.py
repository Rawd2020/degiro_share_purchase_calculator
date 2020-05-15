# Main kick off code for the Degiro fee calulator
# Created By: Rory Williams Doyle.

from gui import gui
from dataDownloader import downloader
from feeSchedualParser import parseFees


def main():
    """
    Main setup code for the fee calculator
    """
    
    downloader()
    fees = parseFees()
    gui(fees)

if __name__ == "__main__":
    main()