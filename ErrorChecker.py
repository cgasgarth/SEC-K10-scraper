import os
from openpyxl import *

class ErrorChecker:
    def checkMissing(stockList, directory):
        folders = []
        for x in os.listdir(directory):
            folders.append(x)
        missedStocks = []
        for i in stockList:
            if i.return_ipo_name().upper() not in folders:
                missedStocks.append(i)
        return missedStocks

    def checkMissingTest(stockList, directory):
        folder = []
        for x in os.listdir(directory):
            folder.append(x)

        print("Printing folders")
        for i in folder:
            print(i)
        print("Checking Folders")
        missedStocks = []
        for i in stockList:
            if i.return_ipo_name().upper() not in folder:
                missedStocks.append(i)
        return missedStocks