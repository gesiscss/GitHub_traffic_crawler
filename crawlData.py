import sys
from DataRetrieval import setupConfigFile as setup
from Visualization import basicPlot as visual
import os

def mainMethod():
    setup.generateConfigFiles()
    setup.updateBatFile()
    setupBat = os.path.dirname(os.getcwd())+"/GesisTraffic/setup.bat"
    os.system(setupBat)
    visual.runVisualization()

mainMethod()