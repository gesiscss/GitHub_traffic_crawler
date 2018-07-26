import requests
import json
from DataRetrieval import readJson
import pandas as pd

def retrieveRepositoriesList():

    response = requests.get("https://api.github.com/orgs/gesiscss/repos").json()
    #print("Response: ", response)
    #API can sometimes reply with - rate limit exceeded for this server.. make an offline json file
    dataFrame = pd.DataFrame.from_dict(response)
    listOfRepositories = dataFrame['archive_url'].values
    listOfRepositories = [getShortNameRepository(repository) for repository in listOfRepositories]
    return listOfRepositories

def getShortNameRepository(fullPath):
    return fullPath.split('gesiscss/', 1)[1].split('/',1)[0]

def getRequestContributors():

    repos = [repo['name'] for repo in requests.get("https://api.github.com/orgs/gesiscss/repos").json()]
    path = "https://api.github.com/repos/gesiscss/" + repos[0] + "/stats/contributors"
    response = requests.get(path).json()
    print(response,"\n\n\n\n")
    #API can sometimes reply with - rate limit exceeded for this server.. make an offline json file
    dataFrame = pd.DataFrame.from_dict(response)
    # listOfRepositories = dataFrame['archive_url'].values
    # listOfRepositories = [getShortNameRepository(repository) for repository in listOfRepositories]
    return dataFrame

print(getRequestContributors())



