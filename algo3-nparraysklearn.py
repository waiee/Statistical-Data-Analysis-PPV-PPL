### -- Python -- ###

import csv
import math
import pandas as pd
import timeit
import haversine as hs
import array
import numpy
from sklearn.metrics.pairwise import haversine_distances

# import asyncore
# import asyncio

# == Note == #

# To change due to modification:
# 1 - Filename
# 2 - Distance formula


# -- START TIME -- #
start = timeit.default_timer()


# - Constant - File Name - #
PEOPLE_FILENAME = 'people.csv'
PPV_FILENAME    = 'ppv.csv'


# --------- FUNCTIONS --------- #

def countNumOfRow(filename):

    numOfRow = 0
    file = open(filename)
    csvreader = csv.reader(file)
    headerList = next(csvreader)

    for row in csvreader:
        numOfRow += 1
    
    return numOfRow


def retrieveData(filename,headerList,dataLaLoList):
    
    rowCounter = 0

    file = open(filename)
    csvreader = csv.reader(file)
    headerList = next(csvreader)

    for row in csvreader:
        # -- Change data format = from STRING to FLOAT
        row.pop(0)
        row.append(float(row[0]))
        row.append(float(row[1]))
        row.pop(0)
        row.pop(0)
        dataLaLoList[rowCounter][0] = row[0]
        dataLaLoList[rowCounter][1] = row[1]

        rowCounter += 1


def distanceFormula(lat1,lon1,lat2,lon2):

    d = 0.00
    point1 = numpy.array([lat1,lon1])
    point2 = numpy.array([lat2,lon2])

    point1Rad = numpy.array([math.radians(x) for x in point1])
    point2Rad = numpy.array([math.radians(y) for y in point2])

    temp = haversine_distances([point1Rad,point2Rad])
    d = temp[0][1]
    return d


def calcShortestSphericalDistance(dataLaLoPeople,dataLaLoPPV,numOfPeople,numOfPPV):

    matchedPeoplePPV = numpy.zeros([numOfPeople,2])
    d  = 0.00
    shortestDistance = 0.00
    nearestPPV = 0.00

    peopleCounter = 0
    PPVCounter    = 0

    for i in range(numOfPeople):

        d = 0
        shortestDistance = 0
        PPVCounter = 0
        nearestPPV = 0

        lat1 = dataLaLoPeople[i][0]
        lon1 = dataLaLoPeople[i][1]

        for j in range(len(dataLaLoPPV)):

            lat2 = dataLaLoPPV[j][0]
            lon2 = dataLaLoPPV[j][1]

            d = distanceFormula(lat1,lon1,lat2,lon2)

            if shortestDistance == 0.00:
                shortestDistance = d
                nearestPPV = 0
            else:
                if d < shortestDistance:
                    shortestDistance = d
                    nearestPPV = PPVCounter

            PPVCounter += 1

        matchedPeoplePPV[i][0] = peopleCounter
        matchedPeoplePPV[i][1] = nearestPPV
        peopleCounter += 1

    return matchedPeoplePPV
    
# ------------------------------#


# - Retrieve data from files - #

numOfPeople = countNumOfRow(PEOPLE_FILENAME)
numOfPPV = countNumOfRow(PPV_FILENAME)


# -- People -- #

headerPeople   = []
dataLaLoPeople = numpy.zeros([numOfPeople,2])

retrieveData(PEOPLE_FILENAME,headerPeople,dataLaLoPeople)

df = pd.DataFrame(dataLaLoPeople)
print(df)
print()


# # -- PPV -- #

headerPPV   = []
dataLaLoPPV = numpy.zeros([numOfPPV,2])

retrieveData(PPV_FILENAME,headerPPV,dataLaLoPPV)

df = pd.DataFrame(dataLaLoPPV)
print(df)
print()


# - Calculation - #

matchedPeoplePPV = numpy.zeros([numOfPeople,2])
matchedPeoplePPV = calcShortestSphericalDistance(dataLaLoPeople,dataLaLoPPV,numOfPeople,numOfPPV)
dfmatched = pd.DataFrame(matchedPeoplePPV)
print(dfmatched)
print()


# -- Write to csv file -- #

f = open('matchedPeoplePPV.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['Index','People','PPV'])

indexCounter = 0
for row in matchedPeoplePPV:
    indexCounter += 1
    writer.writerow([indexCounter, row[0], row[1]])


# -- STOP TIME -- #
stop = timeit.default_timer()


# -- Display processing time -- #
print('Time: ', stop - start)

