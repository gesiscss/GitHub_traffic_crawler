import csv
from DataRetrieval import readJson
import pandas as pd
import os
import operator
from DataRetrieval import readRepositories as rr

CSV_FOLDER = os.path.dirname(os.getcwd()) + "\GesisTraffic\gh_traffic\CSV_Files"



def giveFullPandaFiles(type="views"): #return list of tuples with format : (path, concatenated dataframe)
    temporaryListOfDictionaries = []
    finalListOfDictionaries = []
    temporaryKey = ""
    listIterator = -1
    cumulativeValue = 0

    jsonDictionary = readJson.findJsonFiles().items()

    for key, value in jsonDictionary:

        category = readJson.getShortName2(key)[1]
        temporaryPath = readJson.getShortName2(key)[0] + "_" + category

        if(type == category== "views" and isMonthlyFile(key)==True):
            tuple = (temporaryPath, [value])
            if not((temporaryKey==tuple[0])):
                temporaryListOfDictionaries.append(tuple)
                listIterator = listIterator + 1
            else:
                temporaryListOfDictionaries[listIterator][1].append(value)
            temporaryKey = tuple[0]

        if(type == category == "referrers"):
            tuple = (temporaryPath, [value])
            if value.empty: continue
            if not((temporaryKey==tuple[0])):
                temporaryListOfDictionaries.append(tuple)
                listIterator = listIterator + 1
            else:
                temporaryListOfDictionaries[listIterator][1].append(value)
            temporaryKey = tuple[0]

        if(type == category == "clones" and isMonthlyFile(key)==False):
            tuple = (temporaryPath, [value])
            if value.empty: continue

            value['Repository_name'] = readJson.getShortName(key)

            if not((temporaryKey==tuple[0])):
                temporaryListOfDictionaries.append(tuple)
                listIterator = listIterator + 1
            else:
                temporaryListOfDictionaries[listIterator][1].append(value)
            temporaryKey = tuple[0]

    for i,j in temporaryListOfDictionaries:
        concatenatedRows = pd.concat(j).reset_index(drop=True)
        if(type=="referrers"):
            concatenatedRows = concatenatedRows.groupby('referrer', as_index=False).sum()
        if (type == "clones"):
            concatenatedRows = concatenatedRows.groupby('Repository_name', as_index=False).sum()
        finalListOfDictionaries.append((i, concatenatedRows))

    del temporaryListOfDictionaries[:]
    return finalListOfDictionaries

def concatDataFrameLists(list):
    cumulativeValue = 0
    for df in list:
        cumulativeValue = df.iloc[[-1][0]]
        print(df, "\n\n\n")

def isMonthlyFile(jsonFile):
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

def writeToCSVFileContributors(df):

    nameOfTheFile = CSV_FOLDER + "\General\Contributions.csv"
    print(nameOfTheFile)

    if df is not None:
        with open(nameOfTheFile, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='\t',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        df.to_csv(nameOfTheFile, sep='\t', encoding='utf-8', index=False)

    return df

def sortAndReturnRepositories(csvFiles, inverse = False):
    #csvFiles = giveFullPandaFiles(type=by)
    dictionary = []  # dictionary that will consist only of file name and value:sum of views

    for csvFile, df in csvFiles:
        dictionary.append((csvFile, df['count'].sum()))

    if (inverse==True): sorted_x = sorted(dictionary, key=operator.itemgetter(1), reverse=False)
    else: sorted_x = sorted(dictionary, key=operator.itemgetter(1), reverse=True)
    return sorted_x


