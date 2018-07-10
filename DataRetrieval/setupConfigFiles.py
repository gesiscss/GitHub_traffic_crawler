from DataRetrieval import readRepositories as rr
import configparser
import os
from subprocess import Popen

CONFIG_FILES_FOLDER = os.path.dirname(os.getcwd()) + "\gh_traffic\configFiles\\"
BAT_FILE_PATH = "C:\\Users\\popovirr\\PycharmProjects\\GesisTraffic\\setup.bat"

def readRepositoriesFromConfig():
    Config = configparser.ConfigParser()
    Config.read(os.path.dirname(os.getcwd()) + "\gh_traffic\config.ini")
    section = Config.sections()[0]
    return Config.get(section, 'repository').split("/")[-1]

def generateConfigFiles():

    config = configparser.ConfigParser()
    repositories = rr.retrieveRepositoriesList()
    for repository in repositories:
        config['github'] = {}
        config['github']['token'] = ' 97347e59e82e7352a00c1803597ff51d0f3c9d7e '  # update
        config['github']['repository'] = 'gesiscss/'+repository  # create
        with open(CONFIG_FILES_FOLDER + repository + "_config.ini", 'w') as configfile:  # save
            config.write(configfile)

def updateBatFile():

    SETUP_BAT_PHRASE_FIRST_PART = "github_get_traffic -c gh_traffic/configFiles/"
    SETUP_BAT_PHRASE_LAST_PART = "_config.ini -o gh_traffic"
    SETUP_BAT_FULL_PHRASE = ""
    setupBathPath = os.path.dirname(os.getcwd()) + "\setup.bat"

    repositories = rr.retrieveRepositoriesList()

    with open(setupBathPath, 'w') as the_file:
        the_file.write("")

    for i, repository in enumerate(repositories):
        print(i)
        SETUP_BAT_FULL_PHRASE = SETUP_BAT_PHRASE_FIRST_PART + repository + SETUP_BAT_PHRASE_LAST_PART
        FULL_STRING = ""
        with open(setupBathPath, 'a') as the_file:
            FULL_STRING = FULL_STRING + SETUP_BAT_FULL_PHRASE+"\n"
        print(FULL_STRING)

    the_file.close()
    return setupBathPath

#this method does not work for some reason
#def runBatchFile():
    #setupBatPath = updateBatFile()
    #print(BAT_FILE_PATH)
    #p = Popen(BAT_FILE_PATH)
    #stdout, stderr = p.communicate()

#generateConfigFiles()
#runBatchFile()