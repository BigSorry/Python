import random
import matplotlib.pyplot as plt
import numpy as np

def GeneratePoints(amount):
    result = np.ones((amount, 4))
    for i in range(amount):
        result[i][1] = np.random.uniform(-1, 1)
        result[i][2] = np.random.uniform(-1, 1)
    return result

def Hypothesis(weightVector, point):
    dot = (weightVector[0] * point[0]) + (weightVector[1] * point[1]) + (weightVector[2] * point[2])
    if dot > 0:
        return 1
    else:
        return -1

def UpdateWeight(weight, wrongPoint):
    newWeight = np.array([0.0,0.0,0.0])
    #wrongPoint[3] = is Yn for a Xn
    newWeight[0] = weight[0] + wrongPoint[3]
    newWeight[1] = weight[1] + (wrongPoint[1] * wrongPoint[3])
    newWeight[2] = weight[2] + (wrongPoint[2] * wrongPoint[3])
    return  newWeight

def Classify(trainingVector):
    twoSamples = [[random.uniform(-1, 1) for i in range(2)] for i in range(2)]
    slope = (twoSamples[1][1] - twoSamples[0][1]) / (twoSamples[1][0] - twoSamples[0][0])
    lineStart = twoSamples[0][1] - (twoSamples[0][0] * slope)
    for point in trainingVector:
        difference = point[2] - (slope * point[1] + lineStart)
        if difference > 0:
            point[3] = 1
        else:
            point[3] = -1
    #plt.plot([-1, 1], [lineStart - slope, lineStart + slope])
    #plt.axis([-1.0, 1.0, -1, 1])

n = 100
runs = 1000
maxIters = 240
errors = 0
for i in range(runs):
    points = GeneratePoints(n)
    weigthVector = np.array([0.0,0.0,0.0])
    Classify(points)
    #plt.scatter(points[:, [1]], points[:, [2]], c = points[:, [3]])
    #plt.show()
    errorList = list()
    for j in range(maxIters):
        for point in points:
            hypo = Hypothesis(weigthVector, point)
            if(hypo != point[3]):
                errorList.append(point)
        if len(errorList) > 0:
            errPoint = random.choice(errorList)
            weigthVector = UpdateWeight(weigthVector, errPoint)
    # check training
    for point in points:
        hypo = Hypothesis(weigthVector, point)
        if(hypo != point[3]):
            errors += 1



print("Total average errors by the Learning from data: %s" % (errors / runs))
print("Percentage errors from the test data by Learning from data: %s" % ((errors / runs) / n))


