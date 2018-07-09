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

    df = readJson.giveDataFrameExample()
    print(df)

    # #print(type(dateutil.parser.parse('2018-07-06T00:00:00Z', ignoretz=True)))
    # #print(dates)
    # datenums = md.date2num(dates)
    # values = np.sin((timestamps - now) / duration * 2 * np.pi)
    # plt.subplots_adjust(bottom=0.2)
    # plt.xticks(rotation=25)
    # ax = plt.gca()
    # xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    # ax.xaxis.set_major_formatter(xfmt)
    # plt.plot(datenums, values)
    # plt.show()

def testPlotter():
    dfex = readJson.giveDataFrameExample()
    df = dfex.cumsum()
    plt.figure()
    df.plot()
    plt.legend(loc='best')

#timeStampPlotter()
#testPlotter()


