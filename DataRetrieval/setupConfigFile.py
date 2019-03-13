from DataRetrieval import readRepositories as rr
import configparser
import subprocess
import os
import sys
from subprocess import Popen

CONFIG_FILES_FOLDER = os.path.abspath(__file__ + "/../..") + "/gh_traffic/configFiles/"
#GET_TRAFFIC_METHOD_PATH = os.path.abspath(__file__ + "/../../..") + "/anaconda3/bin/"

#BAT_FILE_PATH = "/setup.bat"

def readRepositoriesFromConfig():
    Config = configparser.ConfigParser()
    Config.read(os.path.dirname(os.getcwd()) + "/gh_traffic/config.ini")
    section = Config.sections()[0]
    return Config.get(section, 'repository').split("/")[-1]

def generateConfigFiles():
    ### creates config files from repositories using API ###
    config = configparser.ConfigParser()
    repositories = rr.retrieveRepositoriesList()
    for repository in repositories:
        config['github'] = {}
        config['github']['repository'] = 'gesiscss/'+repository
        token = rr.getToken()
        config['github']['token'] = token# create
        with open(CONFIG_FILES_FOLDER + repository + "_config.ini", 'w') as configfile:  # save
            config.write(configfile)

#Method for running the GET call for each of the repositories, without writing on a .bat file
def updatePythonFile():
    repositories = rr.retrieveRepositoriesList() # from API
    print('\n'.join(repositories[:2]))

    external_repositories = rr.retrieveExternalRepositoriesList(repositories, CONFIG_FILES_FOLDER) # from extra config files
    all_repositories = repositories.copy()
    all_repositories.extend(external_repositories)

    print("{} gesiscss repositories.".format(len(repositories)))
    print("{} external repositories.".format(len(external_repositories)))
    print("{} TOTAL repositories.".format(len(all_repositories)))

    SETUP_BAT_PHRASE_FIRST_PART = "{}/bin/github_get_traffic -c ".format(sys.exec_prefix) + CONFIG_FILES_FOLDER
    SETUP_BAT_PHRASE_LAST_PART = "_config.ini -o gh_traffic/Repositories/"
    SETUP_BAT_FULL_PHRASE = ""

    for i, repository in enumerate(all_repositories):
        SETUP_BAT_FULL_PHRASE = SETUP_BAT_PHRASE_FIRST_PART + repository + SETUP_BAT_PHRASE_LAST_PART + repository
        command = SETUP_BAT_FULL_PHRASE.split(" ")
        print("Command is: ", SETUP_BAT_FULL_PHRASE)
        subprocess.call(command)

    print("Output is available in gh_traffic/Repositories")
    return all_repositories


# CURRENTLY NOT USED Writing on a .bat file list of commands
def updateBatFile():

    SETUP_BAT_PHRASE_FIRST_PART = "{}/bin/github_get_traffic -c gh_traffic/configFiles/".format(sys.exec_prefix)
    SETUP_BAT_PHRASE_LAST_PART = "_config.ini -o gh_traffic"
    SETUP_BAT_FULL_PHRASE = ""
    setupBatFile = os.path.dirname(os.getcwd()) + "/GitHub_traffic_crawler/setup.bat"

    print("Bat file location:", setupBatFile)

    repositories = rr.retrieveRepositoriesList()

    #with open(setupBatFile, 'w') as the_file:
    #    the_file.write("")

    FULL_STRING = ""

    for i, repository in enumerate(repositories):
        SETUP_BAT_FULL_PHRASE = SETUP_BAT_PHRASE_FIRST_PART + repository + SETUP_BAT_PHRASE_LAST_PART
        FULL_STRING = FULL_STRING + SETUP_BAT_FULL_PHRASE+"\n"
    with open(setupBatFile, 'w') as the_file:
        the_file.write(FULL_STRING)

    with open(setupBatFile, 'r') as the_file:
        if(the_file.read()!=""):
            print("Crawling success!")

    the_file.close()
    return setupBatFile
