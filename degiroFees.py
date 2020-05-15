# A class to represent the fee schedual from the Degiro
# fee schedual PDF.
# Created By: Rory Williams Doyle.

import ast

from config import DATAPATH

class DegiroFees(object):
    """
    A class representing all fees liable to Degiro as listed
    in their fee schedual PDF.
    """
    def __init__(self):
        self.basicFees = {}

    def readStockTable(self, tableId):
        """
        A method to read the fees for ordinary stock,
        leveraged products, etns, warrants & ards from 
        the PDF and to update the basicFees attribute.

        :param tableId: Int ID of the table with the desired values for parsing.
        """

        with open(DATAPATH + "/table_" + str(tableId) + ".json") as f:
            rows = ast.literal_eval(f.readlines()[0])
            for row in rows[1:]:
                formattedExchangeName = ''.join([char for char in row.get("0") if not char.isdigit()]).strip()
                multipleExchangeNames = formattedExchangeName.split(",")

                # Check if we are dealing with multuiple exchanges with the same fees.
                if len(multipleExchangeNames) > 1:
                    for exchangeName in multipleExchangeNames:
                        exchangeName = exchangeName.strip()
                        self.basicFees[exchangeName] = {}
                        self.__updateBasicFees(row, exchangeName)
                else:
                    self.basicFees[formattedExchangeName] = {}
                    self.__updateBasicFees(row, formattedExchangeName)

    def __updateBasicFees(self, row, exchange):
        """
        Update the basicFees attribute with the fixed & variable fees
        for a given exchange and it's max fee value if any.

        :param row: List that is a table row.
        :param exchange: Str that is the name of the exchange.
        """

        fee = row.get("1").split()
        self.basicFees[exchange]["fixedFee"] = fee[1]
        
        # Determine if variable fee is per share or a percentage.
        if fee[-1] == "share":
            self.basicFees[exchange]['perShareFee'] = float(fee[-3])
        else:
            self.basicFees[exchange]['percentageFee'] = float(fee[-1][:-1])/100

        # Determine max allowable fee if any.
        maxFee = row.get("2").split()
        if len(maxFee) > 1:
            self.basicFees[exchange]['maxFee'] = float(maxFee[-1])
