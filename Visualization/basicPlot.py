from DataRetrieval import readJson
import matplotlib as mat
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt
import pandas as pd
import time
import numpy as np
import dateutil.parser
import os
from datetime import datetime

#these are not constant values should be changed
IMAGES_FOLDER = os.path.dirname(os.getcwd())+"\Visualization\Images\\"
#REPOSITORY_NAME = readJson.receiveRepositoryName()+"\\"

def timeStampPlotter():

    n = 20
    duration = 1000
    now = time.mktime(time.localtime())
    timestamps = np.linspace(now, now + duration, n)
    dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]

def testPlotterCumulativeCount():

    for key, value in readJson.findJsonFiles().items():
        subcategory = readJson.getShortName2(path=key)[1]
        name = readJson.getShortName(path=key)
        df = value

        if(df.values.size==0):
            print(name, " has empty values")
            continue

        timestampValues = df.values[:, 1]

        if(subcategory=='views'):
            if(isinstance(timestampValues[0], pd._libs.tslibs.timestamps.Timestamp)):
                timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]
                example = df.ix[:, 'count']
                test = example.cumsum()
                plt.figure();
                test.plot();
                plt.legend(loc='best')

                # fig, ax = plt.subplots()
                # ax.tick_params(labelbottom=False)

                title = "Cumulative count from " + timestampValues[0] + " to " + timestampValues[-1]
                plt.title(title)
                savePlotAsAnImage(plt, name=name, type='cumulative')

def testPlotterHistogram():

    for key, value in readJson.findJsonFiles().items():
        subcategory = readJson.getShortName2(path=key)[1]
        name = readJson.getShortName(path=key)
        df = value

        if(df.values.size==0):
            continue

        timestampValues = df.values[:, 1]


        if(subcategory=='views'):
            if (isinstance(timestampValues[0], pd._libs.tslibs.timestamps.Timestamp)):
                timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]
                df = df.drop('timestamp', 1)
                fig, axes = plt.subplots(nrows=2, ncols=1)
                for i, c in enumerate(df.columns):
                    df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c.upper())
                    if (i == len(df.columns) - 1):
                        axes[i].set_xticklabels(timestampValues)
                    else:
                        axes[i].set_xticklabels([])
                savePlotAsAnImage(plt, name=name, type='histogram')

def testPlotterHistogram2():
    colors = ['red', 'tan', 'lime']
    n_bins = 3
    name = readJson.giveDataFrameExample()[0]
    df = readJson.giveDataFrameExample()[1]

    timestampValues = df.values[:,1]
    timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]

    df = df.drop('timestamp', 1)
    fig, axes = plt.subplots(nrows=2, ncols=1)

    for i, c in enumerate(df.columns):
        df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c.upper())
        if (i == len(df.columns) - 1):
            axes[i].set_xticklabels(timestampValues)
        else:
            axes[i].set_xticklabels([])

    savePlotAsAnImage(plt, name=name, type='histogram')

def savePlotAsAnImage(plt, name, type):

    newpath = IMAGES_FOLDER+"\\"+type+"\\"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    fullPathAndName =  newpath+str(name)+"_"+type+".png"
    plt.savefig(fullPathAndName)

#def runPlotForEveryRepository():


#testPlotterCumulativeCount()
testPlotterHistogram()


