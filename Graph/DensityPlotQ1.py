# ------------------------------------------------------------------- #

import csv
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# == Data files name == #

FILENAME1 = 'comp1.csv'
FILENAME2 = 'comp2.csv'

def retrieveData(filename,headerList,dataLaLoList,numOfRow):
    
    file = open(filename)
    csvreader = csv.reader(file)
    headerList = next(csvreader)

    for row in csvreader:
        numOfRow += 1
        # -- Change data format = from STRING to FLOAT
        row.append(float(row[0]))
        row.pop(0)
        dataLaLoList.append(row)

time1 = []
header1 = []
numOfRow1 = 0
retrieveData(FILENAME1,header1,time1,numOfRow1)

dfTime1 = pd.DataFrame(time1)
dfTime1.columns = ['Times (s)']

time2 = []
header2 = []
numOfRow2 = 0
retrieveData(FILENAME2,header2,time2,numOfRow2)

dfTime2 = pd.DataFrame(time2)
dfTime2.columns = ['Times (s)']

p = sns.kdeplot(dfTime1['Times (s)'], shade = True, color='blue', label = 'Computer 1')
p = sns.kdeplot(dfTime2['Times (s)'], shade = True, color='yellow', label = 'Computer 2')

# == Additional setting == #

# plt.figure(figsize=(10,8)) # ----------------------- Resize Graph Figure -----------
# p.set_xlabel("Times", fontsize = 10) # ------------- Additional Distplot Commmand -- 
# plt.xticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]) # -- Manual x-axis scale -----------

# ======================== #

sns.set_style('darkgrid')
plt.legend()
plt.show()

# ------------------------------------------------------------------- #
