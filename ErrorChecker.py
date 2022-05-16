import os
from StockClass import Stock
from sedScraper import Scraper
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

# def takeAll():
#     stockList = []
#     row = 3
#     while(sheet["A"+str(row)].value!=0):
#         newStock = Stock(sheet["A"+str(row)].value, sheet["B"+str(row)].value, sheet["C"+str(row)].value,
#         sheet["D"+str(row)].value, sheet["E"+str(row)].value, sheet["F"+str(row)].value,
#         sheet["G"+str(row)].value, sheet["H"+str(row)].value, sheet["I"+str(row)].value,
#         sheet["L"+str(row)].value, sheet["M"+str(row)].value)
#         stockList.append(newStock)
#         row += 1
#     return stockList
# workbook = load_workbook(filename="StocksInfo.xlsx")
# print(workbook.sheetnames)
# sheet = workbook.active
# print(sheet)
# stockList = takeAll()
# missingStocks = ErrorChecker.checkMissingTest(stockList, './sec-edgar-filings')
# print('----------------------------------------------')
# for i in missingStocks:
#     print(i.return_ipo_name().upper())
