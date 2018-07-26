from DataRetrieval import readJson
from DataRetrieval import csvManipulation
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
import sys
from PIL import Image
import math

from enum import Enum

# these are not constant values should be changed
IMAGES_FOLDER = os.path.dirname(os.getcwd()) + "\Visualization\Images\\"


# REPOSITORY_NAME = readJson.receiveRepositoryName()+"\\"
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

        if (df.values.size == 0):
            print(name, " has empty values")
            continue

        timestampValues = df.values[:, 1]

        if (subcategory == 'views'):
            if (isinstance(timestampValues[0], pd._libs.tslibs.timestamps.Timestamp)):
                timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]
                example = df.ix[:, 'count']
                test = example.cumsum()
                plt.figure();
                test.plot();
                plt.legend(loc='best')

                # fig, ax = plt.subplots()
                # ax.tick_params(labelbottom=False)

                title = "Info from " + timestampValues[0] + " to " + timestampValues[-1] + " \nfor " + " : " + name
                plt.title(title)
                savePlotAsAnImage(plt, name=name, type='cumulative')


def testPlotterHistogram():
    for key, value in readJson.findJsonFiles().items():
        subcategory = readJson.getShortName2(path=key)[1]
        name = readJson.getShortName(path=key)
        df = value

        if (df.values.size == 0):
            continue

        timestampValues = df.values[:, 1]

        if (subcategory == 'views'):
            if (isinstance(timestampValues[0], pd._libs.tslibs.timestamps.Timestamp)):
                timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]
                df = df.drop('timestamp', 1)
                fig, axes = plt.subplots(nrows=2, ncols=1)
                for i, c in enumerate(df.columns):
                    df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c.upper() + " : " + name)

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

    timestampValues = df.values[:, 1]
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

    newpath = IMAGES_FOLDER + "\\" + type + "\\"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    fullPathAndName = newpath + str(name) + "_" + type + ".png"
    plt.savefig(fullPathAndName, bbox_inches='tight')


def mergePngFiles(type):
    images_list = readJson.findPngFiles(type)
    imgs = [Image.open(i) for i in images_list]
    dimension = int(math.sqrt(math.ceil(len(images_list))))
    listOfHorizontalImages = []

    for k in range(dimension):
        min_img_shape = sorted([(np.sum(i.size), i.size) for i in imgs[k:dimension + k]])[0][1]
        img_merge = np.hstack((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imgs[k:dimension + k]))

        # save the horizontally merged images
        img_merge = Image.fromarray(img_merge)
        path = str(k) + "temporary.png"
        listOfHorizontalImages.append(path)
        img_merge.save(path)

    imgs = [Image.open(i) for i in listOfHorizontalImages]
    min_img_shape = sorted([(np.sum(i.size), i.size) for i in imgs[0:dimension]])[0][1]
    img_merge = np.vstack((np.asarray(i.resize(min_img_shape, Image.ANTIALIAS)) for i in imgs))
    img_merge = Image.fromarray(img_merge)
    img_merge.save("Full_" + type + ".png")

    dirTest = os.path.dirname(os.getcwd()) + "\Visualization\\"
    for file in os.listdir(os.path.dirname(dirTest)):
        if file.endswith('temporary.png'):
            print(file)
            os.remove(file)


def visualizeCSV():

    pandaFiles = csvManipulation.giveFullPandaFiles()

    for key, value in pandaFiles:

        print(key)

        name = key
        df = value

        timestampValues = df.values[:, 1]
        if (df.values.size == 0):
            print(name, " has empty values")
            continue

        timestampValues = df.values[:, 1]

        if (isinstance(timestampValues[0], pd._libs.tslibs.timestamps.Timestamp)):
            timestampValues = [str(timeStampValue.date()) for timeStampValue in timestampValues]
            example = df.ix[:, 'count']
            test = example.cumsum()

            plt.figure();
            frame = plt.gca()
            frame.axes.get_xaxis().set_visible(False)
            test.plot();
            plt.legend(loc='best')

            # fig, ax = plt.subplots()
            # ax.tick_params(labelbottom=False)

            title = "Info from " + timestampValues[0] + " to " + timestampValues[-1] + " \nfor " + " : " + name
            plt.title(title)
            savePlotAsAnImage(plt, name=name, type='')

def histogramMostViewedRepositories():

    repositories = csvManipulation.sortAndReturnRepositoriesByViews()

    title = "Data from: 29th June - today"
    y = [item[1] for item in repositories][0:8]
    x = [item[0] for item in repositories][0:8]

    x_pos = np.arange(len(x))
    fig, ax = plt.subplots()

    ax.barh(x_pos, y, align='center')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(x)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Views')
    plt.title(title)

    savePlotAsAnImage(plt, name='TopRepositories', type='histogram')

# def runPlotForEveryRepository():


# testPlotterCumulativeCount()
# testPlotterHistogram()
mergePngFiles("cumulative")

#visualizeCSV()

#histogramMostViewedRepositories()