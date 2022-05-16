import os

class Organizer:
    def getYear(folderName):
        stringSplit = folderName.split('-')
        return stringSplit[1]

    def rename(directory):
        stockFolders = []
        for i in os.listdir(directory):
            stockFolders.append(i)
        for i in stockFolders:
            filingTypes = []
            for x in os.listdir(directory+i+"/"):
                filingTypes.append(x)
            for x in filingTypes:
                filingFolders = []
                for y in os.listdir(directory+i+'/10-K/'):
                    filingFolders.append(y)
                for y in filingFolders:
                    path = directory + i +'/'+ x + '/' + y + '/'
                    year = Organizer.getYear(y)
                    os.rename(path + 'filing-details.html', path + i + "-" + x \
                    + "-"+year+'.html')
    def moveFiles(downloaderDir, destinationDir):
        stockFolders = []
        for i in os.listdir(downloaderDir):
            stockFolders.append(i)
        for i in stockFolders:
            filingTypes = []
            for x in os.listdir(downloaderDir+i+"/"):
                filingTypes.append(x)
            for x in filingTypes:
                filingFolders = []
                for y in os.listdir(downloaderDir+i+'/10-K/'):
                    filingFolders.append(y)
                for y in filingFolders:
                    path = downloaderDir + i +'/'+ x + '/' + y + '/'
                    year = Organizer.getYear(y)
                    fileName = i + "-" + x + "-" + year + '.html'
                    os.rename(path + fileName, destinationDir + fileName)