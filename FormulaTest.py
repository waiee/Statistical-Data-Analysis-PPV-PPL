# -- Formula Test -- #

# - Law of Cosine - #
# math.acos(math.sin(latP)*math.sin(latPPV1) + math.cos(latP)*math.cos(latPPV1)*math.cos(lonPPV1-lonP)) * 6371000

# - Haversine formula - #

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