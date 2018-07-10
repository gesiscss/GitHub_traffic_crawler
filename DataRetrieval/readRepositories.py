import requests
import json
from DataRetrieval import readJson
import pandas as pd

def retrieveRepositoriesList():

    response = requests.get("https://api.github.com/orgs/gesiscss/repos").json()

    #API can sometimes reply with - rate limit exceeded for this server.. make an offline json file
    dataFrame = pd.DataFrame.from_dict(response)
    listOfRepositories = dataFrame['archive_url'].values
    listOfRepositories = [getShortNameRepository(repository) for repository in listOfRepositories]
    return listOfRepositories

def getShortNameRepository(fullPath):
    return fullPath.split('gesiscss/', 1)[1].split('/',1)[0]


