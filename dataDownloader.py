# A function for downloading external data to be used
# in the application, e.g. The Degiro fee schedual.
# Created By: Rory Williams Doyle.

import requests
from pathlib import Path

from config import FEEURL, FEEPDFPATH


def downloader():
    """
    Downloads external files.
    
    :return: Nothing.
    :rtype: None.
    """
    # Download the Degiro fee schedual
    print("INFO - Updating fee file.")
    try:
        r = requests.get(FEEURL, stream=True)
        with open(FEEPDFPATH, 'wb') as f:
            f.write(r.content)
        print("INFO - Fee file updated.")
    except requests.exceptions.RequestException as e:
        if not Path(FEEPDFPATH).is_file():
            raise SystemExit(e)
        else:
            print("WARNING - Failed to update fee file. Using current fee file from directory.")
