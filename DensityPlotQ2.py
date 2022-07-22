# ------------------------------------------------------------------- #

import csv
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# == Change file name == #

FILENAME1 = 'method1.csv'
FILENAME2 = 'mehtod2.csv'
FILENAME3 = 'mehtod3.csv'

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
dfTime1.columns = ['Times']

# print(time1) --------------------------------------- Stud ---------------------------

time2 = []
header2 = []
numOfRow2 = 0
retrieveData(FILENAME2,header2,time2,numOfRow2)

dfTime2 = pd.DataFrame(time2)
dfTime2.columns = ['Times']

# print(time2) --------------------------------------- Stud ---------------------------

time3 = []
header3 = []
numOfRow3 = 0
retrieveData(FILENAME3,header3,time3,numOfRow3)

dfTime3 = pd.DataFrame(time3)
dfTime3.columns = ['Times']

# print(time2) --------------------------------------- Stud ---------------------------


# ====== Sample Used (Google, Waiee and Edit) ====== #

# plt.figure(figsize=(10,8)) ------------------------- Resize Graph Figure ------------

p = sns.kdeplot(dfTime1['Times'], shade = True, color='blue')
p = sns.kdeplot(dfTime2['Times'], shade = True, color='yellow')
p = sns.kdeplot(dfTime3['Times'], shade = True, color='purple')

# p.set_xlabel("Times", fontsize = 10) --------------- Additional Distplot Commmand --- 

plt.show()

# ================================================== #