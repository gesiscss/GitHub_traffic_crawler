import csv
from DataRetrieval import readJson
import pandas as pd
import os

CSV_FOLDER = os.path.dirname(os.getcwd()) + "\gh_traffic\CSV_Files\\"

def giveFullPandaFiles(): #return list of tuples with format : (path, concatenated dataframe)
    temporaryListOfDictionaries = []
    finalListOfDictionaries = []
    temporaryKey = ""
    listIterator = -1
    for key, value in readJson.findJsonFiles().items():
        temporaryPath = readJson.getShortName2(key)[0] + "_" + readJson.getShortName2(key)[1]
        if(isMonthlyJsonFile(key)):

            tuple = (temporaryPath, [value])

            #print(temporaryKey, " VS ", tuple[0])
            #if its equal to the previous one
            if not((temporaryKey==tuple[0])):
                temporaryListOfDictionaries.append(tuple)
                listIterator = listIterator + 1
            else:
                temporaryListOfDictionaries[listIterator][1].append(value)

            temporaryKey = tuple[0]

    for i,j in temporaryListOfDictionaries:
        finalListOfDictionaries.append((i, pd.concat(j)))

    del temporaryListOfDictionaries[:]
    return finalListOfDictionaries

def isMonthlyJsonFile(jsonFile):
    lastPartName = readJson.getShortName2(jsonFile)[2]
    return (False, True)[lastPartName.count('-')==1]

def writeToCSVFile():
    pandaFiles = giveFullPandaFiles() #list of tuples

    for key,value in pandaFiles:
        nameOfTheFile = CSV_FOLDER + key + ".csv"
        df = value
        with open(nameOfTheFile, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        df.to_csv(nameOfTheFile, sep='\t', encoding='utf-8')

writeToCSVFile()


