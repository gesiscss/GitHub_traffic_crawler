import sys
sys.path.append("home/popovicr/GesisTraffic")

print(sys.path)

from DataRetrieval import setupConfigFile as setup
from Visualization import basicPlot as visual
import os


def mainMethod():
    setup.generateConfigFiles()
    setup.updateBatFile()
    directory = os.path.dirname(os.getcwd()+"\GesisTraffic")
    os.system(directory+"\\setup.bat")
    visual.runVisualization()

def visualizationMethod():
    visual.runVisualization()

#mainMethod()
#visualizationMethod()


#setup.currentDirectory()
def testMethod():
    print("test")
# if __name__ == "__main__":
#     testMethod()
#