import numpy as np
import scipy.io
import os

dataDir = "test/" #"C:/Users/lexme/PycharmProjects/NIST/data/" #
mats = []
for file in os.listdir( dataDir ) :
    mats.append(scipy.io.loadmat(dataDir+file))

test = mats[0]
print(test)
