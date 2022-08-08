# ------------------------------------------------------------------- #

# Sample 1 (Google)

# # libraries & dataset
# import seaborn as sns
# import matplotlib.pyplot as plt

# # set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
# sns.set(style="darkgrid")
# df = sns.load_dataset('iris')
 
# # density plot with shaded area with kdeplot 'shade' parameter
# sns.kdeplot(df['sepal_width'], shade=True)
# plt.show()

# Sample 2 (Google)

# data = np.random.normal(dataFile) #Generating data.
# plt.figure(figsize = (5,5))
# sb.kdeplot(data , bw = 0.5 , fill = True)
# plt.show()

# import seaborn as sb
# import matplotlib.pyplot as plt

# ------------------------------------------------------------------- #

import csv
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

FILENAME = 'method1.csv'

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

dataFile = []
header = []
numOfRow = 0
retrieveData(FILENAME,header,dataFile,numOfRow)

dfDataFile = pd.DataFrame(dataFile)
dfDataFile.columns = ['Times']

# ====== Sample Used (Google, Waiee and Edit) ====== #

# importing libraries
 
# importing diamond dataset from the library
# df = sns.load_dataset(dfDataFile)


# plotting density plot for carat using distplot()
p = sns.kdeplot(dfDataFile['Times'], shade = True, color='green')

sns.set_style('darkgrid')
plt.xticks([0, 10, 20, 30, 40])

# plt.figure(figsize=(6,6)) # -------------------------- Resize Graph Figure ------------
# p.set_xlabel("Times", fontsize = 10) # --------------- Additional Distplot Commmand ---
# print(sns.axes_style())
# plt.xlabel('Purchase amount', fontsize=18)


# visualizing plot using matplotlib.pyplot library
plt.show()

# ------------------------------------------------------------------- #
