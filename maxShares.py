# A function for calculating the max purchasable shares,
# accounting for fees.
# Created By: Rory Williams Doyle.

def maxShares(f, p, ff, vf=None, psf=None, mf=None):
    """
    Max shares calculator function.
    
    :param int f: The total funds avaible to purchase investment.
    :param int p: Price per unit of investment.
    :param int ff: Fixed fee to conduct the purchase.
    :param int vf: Variable percentage fee for the investment between 0 - 1.
    :param int psf: Fee per share (NOTE: May be in forign currency).
    :param int mf: Max allowable fee.
    :return: The max number of shares purchasable, or an error string.
    :rtype: str
    """
    if not f or not p or not ff or (not vf and not psf):
            return "ERROR - Please fill in all text boxes."

    if (not vf and not psf) or (vf and psf):
        return "ERROR - Define either a %fee or fee/share."

    try:
        f = float(f)
        p = float(p)
        ff = float(ff)
        if vf:
            vf = float(vf)
        else:
            psf = float(psf)
        if mf:
            mf = float(mf)
    except ValueError:
        return "ERROR - Only positive real numbers can be entered in the text boxes."

    if f < 0 or p < 0 or ff < 0 or (vf and vf < 0) or (psf and psf < 0) or (mf and mf < 0):
        return "ERROR - Only positive real numbers can be entered in the text boxes."

    fee = 0.0
    fee += ff
    if vf:
        fee += f*vf
    else:
        fee += (((f-ff)/p)*psf)

    if mf and fee > mf:
        fee = mf

    return str(int(((f-fee)/p)))
