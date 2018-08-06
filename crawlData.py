from DataRetrieval import setupConfigFile as setup
from Visualization import basicPlot as visual
import os

#C:\Users\popovirr\PycharmProjects\GesisTraffic\Visualization\Images\cumulative\

def mainMethod():
    setup.generateConfigFiles()
    setup.updateBatFile()
    directory = os.path.dirname(os.getcwd()+"\GesisTraffic")
    os.system(directory+"\\setup.bat")
    visual.mergePngFiles("cumulative")

mainMethod()

