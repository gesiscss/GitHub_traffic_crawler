import requests
import json
from DataRetrieval import readJson
import pandas as pd
import numpy as np

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

        requestData = requests.get("https://api.github.com/orgs/gesiscss/repos")
        repos = []
        if (requestData.status_code == 403):
            print("Unfortunately api gave: ",requestData.status_code)
            return

        repos = [repo['name'] for repo in requestData.json()]

        columnsName = ['repName', 'noOfTotalContributions', 'topContributor', 'noOfTopContributions',
                           '2ndContr', 'noOf2ndContr']
        df = pd.DataFrame(data=[], columns=columnsName)

        counter = 0

        for repo in repos:

            path = "https://api.github.com/repos/gesiscss/" + repo + "/stats/contributors"
            response = requests.get(path).json()

            if (requestData.status_code == 403):
                print("Unfortunately api gave: ", requestData.status_code)
                return

            if (range(len(response) == 0)): continue

            # indexes of max users
            maxUser1 = 0
            maxUser2 = 0
            total = 0

            for i in range(len(response)):

                total = total + response[i]["total"]
                if (response[i]["total"] > response[maxUser1]["total"]):
                    maxUser1 = i
                else:
                    if (response[i]["total"] > response[maxUser2]["total"]):
                        maxUser2 = i

            valuesToAdd = [repo, total, response[maxUser1]["author"]["login"],
                           response[maxUser1]["total"],
                      response[maxUser2]["author"]["login"], response[maxUser2]["total"]]

            total = 0

            if(response[maxUser1]["author"]["login"]==response[maxUser2]["author"]["login"]):
                        valuesToAdd[4] = valuesToAdd[5] = "/"

            df.loc[counter] = valuesToAdd
            counter = counter + 1

        return df



            # API can sometimes reply with - rate limit exceeded for this server.. make an offline json file
            #dataFrame = pd.DataFrame.from_dict(response)
            # listOfRepositories = dataFrame['archive_url'].values
            # listOfRepositories = [getShortNameRepository(repository) for repository in listOfRepositories]


