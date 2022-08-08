### -- Python -- ###

import csv
from hashlib import new
import math
import pandas as pd
import timeit
import haversine as hs

# == Note == #

# To print all rows in data frame, add "to_string()"
# Example: print(dfmatched.to_string())

# To change due to modification:
# 1 - Filename
# 2 - Distance formula

# Data frame cannot be use with Linked List
# Alternative: Table not printed.


# -- START TIME -- #
start = timeit.default_timer()


# - Constant - File Name - #
PEOPLE_FILENAME = 'people.csv'
PPV_FILENAME    = 'ppv.csv'


# --- CLASSES (LINKED LIST) --- #

class Node:

    def __init__(self, lat = None, lon = None):
        self.lat = lat
        self.lon = lon
        self.next_node = None

    def getLatitude(self):
        return self.lat

    def getLongitude(self):
        return self.lon

class SLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, lat, lon):
        new_node = Node(lat, lon)
        
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while (last.next_node):
                last = last.next_node
            last.next_node = new_node

        self.size += 1

    def getSize(self):
        return self.size

    def listPrint(self):
        
        if self.head == None:
            print("No node in linked list.")
        else:
            print_node = self.head
            while (print_node.next_node is not None):
                print(print_node.getLatitude(), end = ', ')
                print(print_node.getLongitude())
                print_node = print_node.next_node
            print(print_node.getLatitude(), end = ', ')
            print(print_node.getLongitude())

    def listPrintFormatted(self):
        
        if self.head == None:
            print("No node in linked list.")
        else:
            print_node = self.head
            while (print_node.next_node is not None):
                print(str(print_node.getLatitude()).ljust(5), end = ', ')
                print(print_node.getLongitude())
                print_node = print_node.next_node
            print(str(print_node.getLatitude()).ljust(5), end = ', ')
            print(print_node.getLongitude())

    def getHeadLat(self):
        tempNode = self.head
        return tempNode.getLatitude()

    def getHeadLon(self):
        tempNode = self.head
        return tempNode.getLongitude()

    def traverseSpecificNodes(self, times):
        tempNode = self.head
        for i in range(times):
            tempNode = tempNode.next_node
        return tempNode


# --------- FUNCTIONS --------- #

def retrieveData(filename,headerList,dataLaLoList,numOfRow):
    
    file = open(filename)
    csvreader = csv.reader(file)
    headerList = next(csvreader)

    for row in csvreader:
        numOfRow += 1

        floatLat = float(row[1])
        floatLon = float(row[2])

        dataLaLoList.add(floatLat, floatLon)


def distanceFormula(lat1,lon1,lat2,lon2):

    d = 0.00
    point1 = (lat1,lon1)
    point2 = (lat2,lon2)
    d = hs.haversine(point1,point2)
    return d


def calcShortestSphericalDistance(dataLaLoPeople,dataLaLoPPV):

    matchedPeoplePPV = SLinkedList()
    d  = 0.00
    shortestDistance = 0.00
    nearestPPV = 0.00

    peopleCounter = 0
    PPVCounter    = 0

    for i in range(dataLaLoPeople.getSize()):

        tempNotePeople = dataLaLoPeople.traverseSpecificNodes(i)

        d = 0
        shortestDistance = 0.00
        PPVCounter = 0
        nearestPPV = 0

        lat1 = tempNotePeople.getLatitude()
        lon1 = tempNotePeople.getLongitude()

        for j in range(dataLaLoPPV.getSize()):

            tempNotePPV = dataLaLoPPV.traverseSpecificNodes(j)

            lat2 = tempNotePPV.getLatitude()
            lon2 = tempNotePPV.getLongitude()

            d = distanceFormula(lat1,lon1,lat2,lon2)

            if shortestDistance == 0.00:
                shortestDistance = d
                nearestPPV = 0
            else:
                if d < shortestDistance:
                    shortestDistance = d
                    nearestPPV = PPVCounter

            PPVCounter += 1

        matchedPeoplePPV.add(peopleCounter,nearestPPV)
        peopleCounter += 1

    return matchedPeoplePPV
    
# # ------------------------------#


# # - Retrieve data from files - #


# # -- People -- #

headerPeople   = []
dataLaLoPeople = SLinkedList()
numOfPeople    = 0

retrieveData(PEOPLE_FILENAME,headerPeople,dataLaLoPeople,numOfPeople)

print('Data of people retrieved.')
print()


# # -- PPV -- #

headerPPV   = []
dataLaLoPPV = SLinkedList()
numOfPPV    = 0

retrieveData(PPV_FILENAME,headerPPV,dataLaLoPPV,numOfPPV)

print('Data of PPV retrieved.')
print()


# # - Calculation - #

matchedPeoplePPV = SLinkedList()
matchedPeoplePPV = calcShortestSphericalDistance(dataLaLoPeople,dataLaLoPPV)

print('People matched to nearest PPV.')
print()


# -- Write to csv file -- #

f = open('matchedPeoplePPV.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['Index','People','PPV'])

indexCounter = 0
for i in range(matchedPeoplePPV.getSize()):
    indexCounter += 1
    tempNote = matchedPeoplePPV.traverseSpecificNodes(i)
    writer.writerow([indexCounter, tempNote.getLatitude(), tempNote.getLongitude()])


# # -- STOP TIME -- #
stop = timeit.default_timer()


# # -- Display processing time -- #
print('Time: ', stop - start)
