# A function to parse the Degiro Fee schedual PDF
# Created By: Rory Williams Doyle.

import camelot

from config import FEEPDFPATH, DATAPATH
from degiroFees import DegiroFees


def parseFees():
    """
    Parses fees from the Degiro fee schedual PDF.

    :return: A populated DegiroFees object instance.
    :rtype: Object
    """

    tables = camelot.read_pdf(FEEPDFPATH, pages="1-end")
    tableCount = 0  # TODO use this var to process every table & not just the first one.

    # Extract each table from the PDF & convert to JSON
    for index in range(len(tables)):
        tables[index].to_json(DATAPATH + "/table_" + str(index) + ".json")
        tableCount += 1

    fees = DegiroFees()
    fees.readStockTable(0)
    return fees