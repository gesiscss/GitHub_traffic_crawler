import sys
from DataRetrieval import setupConfigFile as setup
from Visualization import basicPlot as visual
import os

def mainMethod():
    setup.generateConfigFiles()
    setup.updateBatFile()
    directory = os.path.dirname(os.getcwd()+"/GesisTraffic")
    os.system(directory+"/setup.bat")
    visual.runVisualization()

def visualizationMethod():
    visual.runVisualization()

mainMethod()
#visualizationMethod()


