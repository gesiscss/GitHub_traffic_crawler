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

IMAGES_FOLDER = os.path.dirname(os.getcwd())+"\Visualization\Images\\"

def timeStampPlotter():

    n = 20
    duration = 1000
    now = time.mktime(time.localtime())
    timestamps = np.linspace(now, now + duration, n)
    dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]

def testPlotterCumulativeCount():

    df = readJson.giveDataFrameExample()
    example = df.ix[:, 'count']
    test = example.cumsum()
    plt.figure();
    test.plot();
    plt.legend(loc='best')
    plt.show()

def testPlotterHistogram():
    colors = ['red', 'tan', 'lime']
    n_bins = 3
    name = readJson.giveDataFrameExample()[0]
    df = readJson.giveDataFrameExample()[1]

    fig, axes = plt.subplots(nrows=3, ncols=1)
    for i, c in enumerate(df.columns):
        if(c == 'timestamp'):
            continue
        df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c)
    savePlotAsAnImage(plt, name=name)

def savePlotAsAnImage(plt, name):
    fullPathAndName =  IMAGES_FOLDER+str(name)+".png"
    print("Full path is: ",fullPathAndName)
    plt.savefig(fullPathAndName)

#timeStampPlotter()
#testPlotterCumulativeCount()
testPlotterHistogram()


