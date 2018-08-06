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

    # try:
            requestData = requests.get("https://api.github.com/orgs/gesiscss/repos")
            print(requestData.status_code)
    #     if(requestData.status_code == 403):
    #         columnsName = ['repName', 'noOfTotalContributions', 'topContributor', 'noOfTopContributions',
    #         '2ndContr', 'noOf2ndContr']
    #         df = pd.DataFrame(data=[], columns=columnsName)
    #
    #         df.loc[0] = [1, 2, 3, 4, 5, 6]
    #         df.loc[1] = [1, 55, 3, 4, 5, 6]
    #         df.loc[2] = [1, 77, 3, 4, 5, 6]
    #
    #         raise Exception
    #         return None
    # except Exception as error:
    #     print("Error: ", requestData.text)  # , error.with_traceback())
    #     return


            repos = [repo['name'] for repo in requestData.json()]
            counter = 0

            columnsName = ['repName', 'noOfTotalContributions', 'topContributor', 'noOfTopContributions',
                           '2ndContr', 'noOf2ndContr']
            df = pd.DataFrame(data=[], columns=columnsName)

            for repo in repos:
                path = "https://api.github.com/repos/gesiscss/" + repo + "/stats/contributors"
                response = requests.get(path).json()

                # indexes of max users
                maxUser1 = 0
                maxUser2 = 0

                for i in range(len(response)):
                    print(response[i]["total"])
                    if (response[i]["total"] > response[maxUser1]["total"]):
                        maxUser1 = i
                    else:
                        if (response[i]["total"] > response[maxUser2]["total"]):
                            maxUser2 = i
                # text = str("\tTotal value for " + response[i]["author"]["login"] +
                #         " 1st most active user: " + response[maxUser1]["author"]["login"] +
                #         " : " + str(response[maxUser1]["total"]))
                # if(maxUser1!=maxUser2):
                #     text = text + str(" and 2nd most active user: " + response[maxUser1]["author"]["login"] + " : " +
                #       str(response[maxUser2]["total"]))

                #print("\t"+text)
                valuesToAdd = [repo, response[i]["total"], response[maxUser1]["author"]["login"], response[maxUser1]["total"],
                          response[maxUser2]["author"]["login"], response[maxUser2]["total"]]

                if(response[maxUser1]["author"]["login"]==response[maxUser2]["author"]["login"]):
                    valuesToAdd[4] = valuesToAdd[5] = "/"

                df.loc[counter] = valuesToAdd

            return df
            # API can sometimes reply with - rate limit exceeded for this server.. make an offline json file
            #dataFrame = pd.DataFrame.from_dict(response)
            # listOfRepositories = dataFrame['archive_url'].values
            # listOfRepositories = [getShortNameRepository(repository) for repository in listOfRepositories]




#print(getRequestContributors())




