import math

# -- People
latP = 4.0
lonP = 6.0

# -- PPV1
latPPV1 = 10.0
lonPPV1 = 2.0

# -- PPV2
latPPV2 = 3.0
lonPPV2 = 9.0

dPtoPPV1 = math.acos(math.sin(latP)*math.sin(latPPV1) + math.cos(latP)*math.cos(latPPV1)*math.cos(lonPPV1-lonP)) * 6371000
dPtoPPV2 = math.acos(math.sin(latP)*math.sin(latPPV2) + math.cos(latP)*math.cos(latPPV2)*math.cos(lonPPV2-lonP)) * 6371000

print('Distance People to PPV1 Sph: ')
print(dPtoPPV1)
print('DIstance People to PPV2 Sph: ')
print(dPtoPPV2)
print()

dEucPtoPPV1 = math.sqrt((latP - latPPV1)**2 + (lonP - lonPPV1)**2)
dEucPtoPPV2 = math.sqrt((latP - latPPV2)**2 + (lonP - lonPPV2)**2)

print('Distance People to PPV1 Euc: ')
print(dEucPtoPPV1)
print('DIstance People to PPV2 Euc: ')
print(dEucPtoPPV2)
print()