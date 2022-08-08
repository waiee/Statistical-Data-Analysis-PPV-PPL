import numpy as np
from sklearn import metrics
import sklearn.neighbors as sk
import math
import pandas as pd

from sklearn.metrics.pairwise import haversine_distances

# -- People
latP = 4.0
lonP = 6.0
people = [latP,lonP]

# -- PPV1
latPPV1 = 10.0
lonPPV1 = 2.0
ppv1 = [latPPV1,lonPPV1]

# -- PPV2
latPPV2 = 3.0
lonPPV2 = 9.0
ppv2 = [latPPV2,lonPPV2]

peopleRad = [math.radians(x) for x in people]
ppv1Rad   = [math.radians(y) for y in ppv1]
ppv2Rad   = [math.radians(z) for z in ppv2]

dfPeople = pd.DataFrame(people)
dfppv1 = pd.DataFrame(ppv1)
dfppv2 = pd.DataFrame(ppv2)

kd1 = haversine_distances([peopleRad,ppv1Rad])
realD1 = kd1[0][1]
print(realD1 * 6371000/1000)
kd2 = haversine_distances([peopleRad,ppv2Rad])
realD2 = kd2[0][1]
print(realD2 * 6371000/1000)