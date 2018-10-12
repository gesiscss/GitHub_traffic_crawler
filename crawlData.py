import sys
import os
import datetime
from DataRetrieval import setupConfigFile as setup

def crawlData():

    setup.generateConfigFiles()
    repositories = setup.updatePythonFile()
    makeReport(repositories)

def makeReport(listOfRepositories):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    TEXT = "For "+ date +" the data has been generated. There are " \
           + str(len(listOfRepositories)) + " repositories available. "
    file = open("report.txt", "a")
    file.write(TEXT+"\n")
    file.close()

crawlData()




