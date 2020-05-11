# A function for calculating the max purchasable shares,
# accounting for fees.
# Created By: Rory Williams Doyle.

def maxShares(f, p, ff, vf):
    """
    Max shares calculator function.
    
    :param int f: The total funds avaible to purchase invetment.
    :param int p: Price per unit of investment.
    :param int ff: Fixed fee to conduct the purchase.
    :param int vf: Variable percentage fee for the investment between 0 - 1.
    :return: The max number of shares purchasable, or an error string.
    :rtype: str
    """
    if not f or not p or not ff or not vf:
            return "ERROR - Please fill in all text boxes."

    try:
        f = float(f)
        p = float(p)
        ff = float(ff)
        vf = float(vf)
    except ValueError:
        return "ERROR - Only positive ints can be entered in the text boxes."

    if f < 0 or p < 0 or ff < 0 or vf < 0:
        return "ERROR - Only positive ints can be entered in the text boxes."

    return(str(int((f-ff-(((f-ff)/p)*vf))/p)))