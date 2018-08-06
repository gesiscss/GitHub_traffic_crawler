import json
from pathlib import Path
import pandas as pd
import os
from enum import Enum

class PlotType(Enum):
    histogram = 1
    cumulative = 2

def readJsonPlain(filename):

    if filename:
        with open(filename, 'r') as f:
            jsonFile = json.load(f)
    #print(jsonFile,"\n\n\n")

def readJsonPanda(jsonPath):

    df = pd.read_json(jsonPath)
    #print(jsonPath, " : \n\n\n", df, "\n\n\n")
    #print(type(df))
    return df

#finds and iterates over json files in folders and subfolders
#and returns a tuple ([ jsonPath, jsonContent ])
# jsonContent is in panda-Dataframe format
def findJsonFiles():

    gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "\gh_traffic\Repositories"
    pathlist = Path(gesisTrafficDirectory).glob('**/*.json')
    jsonFileAndContentInPandaFormat = {}

    for path in pathlist:
        path_in_str = str(path)
        jsonFileAndContentInPandaFormat[path_in_str] = readJsonPanda(path_in_str)
    return jsonFileAndContentInPandaFormat

def findPngFiles(type):

    # if not isinstance(type, Enum):
    #     raise TypeError('direction must be an instance of Direction Enum')
    #
    # print(type.value)
    # raise TypeError('break')
    #gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "\Visualization\Images\cumulative\\"
    gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "\GesisTraffic\Visualization\Images\\"+type+"\\"
    print(gesisTrafficDirectory)
    pathlist = Path(gesisTrafficDirectory).glob('**/*.png')
    pngFileList = []

    return [str(x) for x in pathlist]
    #
    # for path in pathlist:
    #     pngFileList.append = str(path)
    # return pngFileList

def printJsonPaths():
    for key, value in findJsonFiles().items():
        print(key)

def printJsonContent():
    for key, value in findJsonFiles().items():
        print(value)

def printJsonTuple():
    for key, value in findJsonFiles().items():
        print(key,"\n\n\n",value,"\n\n\n")

def giveDataFrameExample():
    for key, value in findJsonFiles().items():
        if(key.__contains__("2018-07.json")):
            return (getShortName(path=key), value)

def getShortName(path):
    #this gets called twice, see why
    substringList = path.split("\\")[-3:len(path)-1:]
    return str(substringList[0]+"_"+substringList[1].split(".json")[0])

def getShortName2(path):
    #this gets called twice, see why
    substringList = path.split("\\")[-3:len(path)-1:]
    return substringList

def dataFrameManipulationTest():
    df = giveDataFrameExample()
    print(df.loc[[0], ['timestamp']])

def giveJsonFilePerRepository():
    listOfKeyValueRepositories = []
    repository = ""
    listOfJsonFilePaths = []
    counter = 0
    for key, value in findJsonFiles().items():

        key = getShortName2(key)
        # dictionaryInstance = { key : value }
        # indexOfListElement = isThereKeyDictionaryValueInList(listOfJsonFilePaths, key)
        # if(indexOfListElement==-1):
        #     listOfJsonFilePaths.append(dictionaryInstance)
        #else:
            #print("Value is: ",value)
            #listOfJsonFilePaths[indexOfListElement].append(value)
        #
        #     listOfJsonFilePaths
        # print("Key", key)
        #listOfJsonFilePaths[counter].append(value)
    return listOfJsonFilePaths

def isThereKeyDictionaryValueInList(list, key):

    counter = 0
    for elem in list:
        for keyString in elem:
            if(keyString == key):
                return counter
        counter = counter + 1
    return -1




#def updatePandaFiles():





#def updateCSV(fileName):


#print(getShortName("C:\\Users\\popovirr\\PycharmProjects\\GesisTraffic\\gh_traffic\\Repositories\\repo2docker\\clones\\2018-07-10.json"))

#printJsonPaths()

# for key, value in findJsonFiles().items():
#     print(getShortName(key))


#list = giveJsonFilePerRepository()
#isThereKeyDictionaryValueInList(list,'workshop_girls_day_views')
#print(list)






