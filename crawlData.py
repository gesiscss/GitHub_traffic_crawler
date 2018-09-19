import sys
import os

from DataRetrieval import setupConfigFile as setup

def crawlData():
    setup.generateConfigFiles()
    setup.updatePythonFile()

crawlData()

