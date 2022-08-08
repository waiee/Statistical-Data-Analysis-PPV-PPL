# ------------------------------------------------------------------- #

import csv
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# == Data files name == #

FILENAME1 = 'method1.csv'
FILENAME2 = 'method2.csv'
FILENAME3 = 'method3.csv'

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

time3 = []
header3 = []
numOfRow3 = 0
retrieveData(FILENAME3,header3,time3,numOfRow3)

dfTime3 = pd.DataFrame(time3)
dfTime3.columns = ['Times (s)']



p = sns.kdeplot(dfTime1['Times (s)'], shade = True, color='blue', label = 'Method 1')
p = sns.kdeplot(dfTime2['Times (s)'], shade = True, color='yellow', label = 'Method 2')
p = sns.kdeplot(dfTime3['Times (s)'], shade = True, color='purple', label = 'Method 3')

# == Additional setting == #

# plt.figure(figsize=(10,8)) # ---------------------------- Resize Graph Figure -----------
# p.set_xlabel("Times", fontsize = 10) # ------------------ Additional Distplot Commmand -- 
# plt.xticks([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20]) # -- Manual x-axis scale -----------

# ======================== #

sns.set_style('darkgrid')
plt.legend()
plt.show()

# ------------------------------------------------------------------- #