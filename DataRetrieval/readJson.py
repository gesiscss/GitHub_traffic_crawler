import json
from pathlib import Path
import pandas as pd
import os

def readJson(filename):

    if filename:
        with open(filename, 'r') as f:
            jsonFile = json.load(f)
    print(jsonFile)

def readJsonPanda(jsonPath):

    df = pd.read_json(jsonPath)
    print(df)

def findJsonFiles():

    gesisTrafficDirectory = os.path.dirname(os.getcwd()) + "\gh_traffic"
    pathlist = Path(gesisTrafficDirectory).glob('**/*.json')
    for path in pathlist:
        path_in_str = str(path)
        readJson(path_in_str)
        #readJsonPanda(path_in_str)

findJsonFiles()