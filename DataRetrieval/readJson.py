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
    return df

#finds and iterates over json files in folders and subfolders
#and returns a tuple ([ jsonPath, jsonContent ])
# jsonContent is in panda-Dataframe format
def findJsonFiles():

    name = os.path.dirname(os.getcwd())
    print("Test name: ", name)
    gesisTrafficDirectory = name + "/GesisTraffic/gh_traffic/Repositories"
    pathlist = Path(gesisTrafficDirectory).glob('**/*.json')
    jsonFileAndContentInPandaFormat = {}

    for path in pathlist:
        path_in_str = str(path)
        jsonFileAndContentInPandaFormat[path_in_str] = readJsonPanda(path_in_str)
    return jsonFileAndContentInPandaFormat

def findPngFiles(type):

    gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "/GesisTraffic/Visualization/Images/"+type
    pathlist = Path(gesisTrafficDirectory).glob('**/*.png')
    pathlistFinal = [str(x) for x in pathlist]

    return pathlistFinal

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
    if (path.__contains__("\\")):
        substringList = path.split("\\")[-3:len(path)-1:]
    else:
        substringList = path.split("/")[-3:len(path) - 1:]
    return str(substringList[0]+"_"+substringList[1].split(".json")[0])

def getShortName2(path):
    #this gets called twice, see why
    if(path.__contains__("\\")):
        substringList = path.split("\\")[-3:len(path)-1:]
    else:
        substringList = path.split("/")[-3:len(path) - 1:]
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
    return listOfJsonFilePaths

def isThereKeyDictionaryValueInList(list, key):

    counter = 0
    for elem in list:
        for keyString in elem:
            if(keyString == key):
                return counter
        counter = counter + 1
    return -1







