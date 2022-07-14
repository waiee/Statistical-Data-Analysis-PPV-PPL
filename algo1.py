### -- Python -- ###

import csv
import math
import pandas as pd
import timeit

# == Note == #

# To run, install panda
# Type in cmd: pip install pandas

# To print all rows in data frame, add "to_string()"
# Example: print(dfmatched.to_string())

# To change due to modification:
# 1 - Filename
# 2 - Distance formula

# -- START TIME -- #
start = timeit.default_timer()


# - Constant - File Name - #
PEOPLE_FILENAME = 'people.csv'
PPV_FILENAME    = 'ppv.csv'


# --------- FUNCTIONS --------- #

def retrieveData(filename,headerList,dataLaLoList,numOfRow):
    
    # numOfRow = 0

    file = open(filename)
    csvreader = csv.reader(file)
    headerList = next(csvreader)

    for row in csvreader:
        numOfRow += 1
        # -- Change data format = from STRING to FLOAT
        row.pop(0)
        row.append(float(row[0]))
        row.append(float(row[1]))
        row.pop(0)
        row.pop(0)
        dataLaLoList.append(row)


def distanceFormula(lat1,lon1,lat2,lon2):
    d = 0.00
    d = math.acos( math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)) * 6371000
    return d


def calcShortestEuclideanDistance(dataLaLoPeople,dataLaLoPPV):

    matchedPeoplePPV = [[]]
    d  = 0.00
    shortestDistance = 0.00
    nearestPPV = 0.00

    peopleCounter = 0
    PPVCounter    = 0

    for i in range(len(dataLaLoPeople)):

        PPVCounter = 0
        nearestPPV = 0

        lat1 = dataLaLoPeople[i][0]
        lon1 = dataLaLoPeople[i][1]

        lat2 = dataLaLoPPV[0][0]
        lon2 = dataLaLoPPV[0][1]

        d = distanceFormula(lat1,lon1,lat2,lon2)
        shortestDistance = d

        for j in range(1,len(dataLaLoPPV)):

            lat1 = dataLaLoPeople[i][0]
            lon1 = dataLaLoPeople[i][1]

            lat2 = dataLaLoPPV[j][0]
            lon2 = dataLaLoPPV[j][1]

            d = distanceFormula(lat1,lon1,lat2,lon2)

            # -- What if sama jarak?
            if d < shortestDistance:
                shortestDistance = d
                nearestPPV = PPVCounter

            PPVCounter += 1

        matchedPeoplePPV.append([peopleCounter,nearestPPV])
        peopleCounter += 1

    matchedPeoplePPV.pop(0) # ----------------------------- Remove the NaN value at index 0
    matchedPeoplePPV.insert(0,['People','Nearest PPV']) # - Header for Data Frame
    return matchedPeoplePPV
    
# ------------------------------#


# - Retrieve data from files - #


# -- People -- #

headerPeople   = []
dataLaLoPeople = []
numOfPeople    = 0

retrieveData(PEOPLE_FILENAME,headerPeople,dataLaLoPeople,numOfPeople)

df = pd.DataFrame(dataLaLoPeople)
print(df)
print()


# -- PPV -- #

headerPPV   = []
dataLaLoPPV = []
numOfPPV    = 0

retrieveData(PPV_FILENAME,headerPPV,dataLaLoPPV,numOfPPV)

df = pd.DataFrame(dataLaLoPPV)
print(df)
print()


# - Calculation - #

matchedPeoplePPV = [[]]
matchedPeoplePPV = calcShortestEuclideanDistance(dataLaLoPeople,dataLaLoPPV)
dfmatched = pd.DataFrame(matchedPeoplePPV)
print(dfmatched)
print()

# -- STOP TIME -- #
stop = timeit.default_timer()

# -- Display processing time -- #
print('Time: ', stop - start)

