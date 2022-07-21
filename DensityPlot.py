# # libraries & dataset
# import seaborn as sns
# import matplotlib.pyplot as plt

# # set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above)
# sns.set(style="darkgrid")
# df = sns.load_dataset('iris')

# # density plot with shaded area with kdeplot 'shade' parameter
# sns.kdeplot(df['sepal_width'], shade=True)
# plt.show()


# import seaborn as sb
# import matplotlib.pyplot as plt

import csv
import numpy as np
import pandas as pd


FILENAME = 'matchedPeoplePPV.csv'
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

dataFile = []
header = []
numOfRow = 0
retrieveData(FILENAME,header,dataFile,numOfRow)

dfDataFile = pd.DataFrame(dataFile)

print(dataFile)

# data = np.random.normal(dataFile) #Generating data.
# plt.figure(figsize = (5,5))
# sb.kdeplot(data , bw = 0.5 , fill = True)
# plt.show()


# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# importing diamond dataset from the library
# df = sns.load_dataset(dfDataFile)

# plt.figure(figsize=(10,8))

# plotting density plot for carat using distplot()
sns.displot(a=dfDataFile, hist=False)

# visualizing plot using matplotlib.pyplot library
plt.show()
