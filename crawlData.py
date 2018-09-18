import sys
import os
from DataRetrieval import setupConfigFile as setup
from Visualization import basicPlot as visual


def crawlData():
    setup.generateConfigFiles()
    setup.updateBatFile()

crawlData()