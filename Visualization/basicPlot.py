from DataRetrieval import readJson
import matplotlib as mat
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt
import pandas as pd
import time
import numpy as np
import dateutil.parser


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

    #np.random.seed(0)
    n_bins = 3
    df = readJson.giveDataFrameExample()
    x = df.ix[0:2, 'count'].values[:,np.newaxis].T

    fig = plt.figure()
    ax0 = fig.add_subplot(111)
    ax0.hist(x, n_bins, histtype='bar')
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    ax0.legend(prop={'size': 3})
    ax0.set_title('View count histogram')
    plt.show()

#timeStampPlotter()
#testPlotterCumulativeCount()
testPlotterHistogram()


