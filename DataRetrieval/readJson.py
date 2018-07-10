import json
from pathlib import Path
import pandas as pd
import os

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

    gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "\gh_traffic"
    pathlist = Path(gesisTrafficDirectory).glob('**/*.json')
    jsonFileAndContentInPandaFormat = {}

    for path in pathlist:
        path_in_str = str(path)
        jsonFileAndContentInPandaFormat[path_in_str] = readJsonPanda(path_in_str)
    return jsonFileAndContentInPandaFormat

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
    substringList = path.split("\\")[-2:len(path)-1:]
    return str(substringList[0]+"_"+substringList[1].split(".json")[0])

def dataFrameManipulationTest():
    df = giveDataFrameExample()
    print(df.loc[[0], ['timestamp']])












