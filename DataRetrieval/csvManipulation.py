import csv
from DataRetrieval import readJson
import pandas as pd
import os
import operator
from DataRetrieval import readRepositories as rr

CSV_FOLDER = os.path.dirname(os.getcwd()) + "\gh_traffic\CSV_Files\\"

def giveFullPandaFiles(): #return list of tuples with format : (path, concatenated dataframe)
    temporaryListOfDictionaries = []
    finalListOfDictionaries = []
    temporaryKey = ""
    listIterator = -1

    cumulativeValue = 0

    for key, value in readJson.findJsonFiles().items():
        category = readJson.getShortName2(key)[1]
        temporaryPath = readJson.getShortName2(key)[0] + "_" + category
        if(category=="views" and isMonthlyJsonFile(key)==True):

            tuple = (temporaryPath, [value])
            #if its equal to the previous one
            if not((temporaryKey==tuple[0])):
                temporaryListOfDictionaries.append(tuple)
                listIterator = listIterator + 1
            else:
                temporaryListOfDictionaries[listIterator][1].append(value)
            temporaryKey = tuple[0]

    for i,j in temporaryListOfDictionaries:
        finalListOfDictionaries.append((i, pd.concat(j).reset_index(drop=True)))

    del temporaryListOfDictionaries[:]
    return finalListOfDictionaries

def concatDataFrameLists(list):
    cumulativeValue = 0
    for df in list:
        cumulativeValue = df.iloc[[-1][0]]
        print(df, "\n\n\n")

def isMonthlyJsonFile(jsonFile):
    lastPartName = readJson.getShortName2(jsonFile)[2]
    if (lastPartName.count('-')==1) :
        return True
    else:
        return False

def writeToCSVFile():
    pandaFiles = giveFullPandaFiles() #list of tuples

    for key,value in pandaFiles:
        nameOfTheFile = CSV_FOLDER + key + ".csv"
        df = value
        with open(nameOfTheFile, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='\t',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        df.to_csv(nameOfTheFile, sep='\t', encoding='utf-8', index=False)

def writeToCSVFileContributors():
    df = rr.getRequestContributors()

    if df is not None:
        nameOfTheFile = CSV_FOLDER + "\Contributors.csv"
        with open(nameOfTheFile, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='\t',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        df.to_csv(nameOfTheFile, sep='\t', encoding='utf-8', index=False)

    return df

def totalNumberOfViewDictionary():
    csvFiles = giveFullPandaFiles()
    dictionary = []  # dictionary that will consist only of file name and value:sum of views
    for csvFile, df in csvFiles:
        dictionary.append((csvFile, df['count'].sum()))
    return dictionary

def sortAndReturnRepositoriesByViews():
    sorted_x = sorted(totalNumberOfViewDictionary(), key=operator.itemgetter(1), reverse=True)
    return sorted_x


#writeToCSVFileContributors()
