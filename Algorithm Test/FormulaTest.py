# -- Formula Test -- #

# - Law of Cosine - #
# math.acos(math.sin(latP)*math.sin(latPPV1) + math.cos(latP)*math.cos(latPPV1)*math.cos(lonPPV1-lonP)) * 6371000

# - Haversine formula - #

import math
import haversine as hs
from geopy import distance
# from haversine import haversine, Unit

def haversine():
    a = (math.sin())

# -- People
latP = 4.0
lonP = 6.0

# -- PPV1
latPPV1 = 10.0
lonPPV1 = 2.0

# -- PPV2
latPPV2 = 3.0
lonPPV2 = 9.0

people = (latP,lonP)
ppv1 = (latPPV1,lonPPV1)
ppv2 = (latPPV2,lonPPV2)

dPtoPPV1 = math.acos(math.sin(latP)*math.sin(latPPV1) + math.cos(latP)*math.cos(latPPV1)*math.cos(lonPPV1-lonP)) * 6371
dPtoPPV2 = math.acos(math.sin(latP)*math.sin(latPPV2) + math.cos(latP)*math.cos(latPPV2)*math.cos(lonPPV2-lonP)) * 6371

print('- Law of cosines -')
print()
print('Distance People to PPV1: ')
print(dPtoPPV1)
print('DIstance People to PPV2: ')
print(dPtoPPV2)
print()

dH1 = hs.haversine(people, ppv1)
dH2 = hs.haversine(people, ppv2)

print('- Haversine formula -')
print()
print('Distance People to PPV1: ')
print(dH1)
print('DIstance People to PPV2: ')
print(dH2)
print()

dG1 = distance.distance(people,ppv1)
dG2 = distance.distance(people,ppv2)

print('- Geodesic formula -')
print()
print('Distance People to PPV1: ')
print(dG1)
print('DIstance People to PPV2: ')
print(dG2)
print()
