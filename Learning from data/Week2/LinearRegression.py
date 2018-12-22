import random
import matplotlib.pyplot as plt
import numpy as np

def GeneratePoints(amount):
    result = np.ones((amount, 4))
    for i in range(amount):
        result[i][1] = np.random.uniform(-1, 1)
        result[i][2] = np.random.uniform(-1, 1)
    return result

def sign(number):
    if number > 0:
        return 1
    else:
        return -1

def nonLinearSign(vector):
    """number = -1 - (0.05 * vector[1]) + (0.08 * vector[2]) + (0.13*vector[1]*vector[2]) +\
             (1.5*vector[1] * vector[1]) + (1.5*vector[2] * vector[2])"""
    number = (vector[1] * vector[1]) + (vector[2] *vector[2]) - 0.6
    return sign(number)

def Hypothesis(weightVector, point):
    #dot = (weightVector[0] * point[0]) + (weightVector[1] * point[1]) + (weightVector[2] * point[2])
    dot = weightVector[0] + weightVector[1]*point[1] + weightVector[2]*point[2] +\
        weightVector[3]*point[3] + weightVector[4]*point[4] + weightVector[5]*point[5]
    return sign(dot)
    #return nonLinearSign(point)

def UpdateWeight(weight, wrongPoint):
    newWeight = np.array([0.0,0.0,0.0])
    #wrongPoint[3] = is Yn for a Xn
    newWeight[0] = weight[0] + wrongPoint[3]
    newWeight[1] = weight[1] + (wrongPoint[1] * wrongPoint[3])
    newWeight[2] = weight[2] + (wrongPoint[2] * wrongPoint[3])
    return  newWeight

def NonLinearClassify(trainingVector):
    transformed = np.zeros([trainingVector.shape[0], 7])
    index = 0
    for point in trainingVector:
        point = np.array([point[0], point[1], point[2], (point[1] * point[2]), (point[1] * point[1]), (point[2] * point[2]), 0])
        number = nonLinearSign(point)
        noise = np.random.randint(1, 10)
        if noise == 1:
            number = number * -1
        point[6] = sign(number)
        transformed[index] = point
        index += 1
    return transformed

def Classify(trainingVector, twoSamples):
    slope = (twoSamples[1][1] - twoSamples[0][1]) / (twoSamples[1][0] - twoSamples[0][0])
    lineStart = twoSamples[0][1] - (twoSamples[0][0] * slope)
    for point in trainingVector:
        difference = point[2] - (slope * point[1] + lineStart)
        point[3] = sign(difference)
    #plt.plot([-1, 1], [lineStart - slope, lineStart + slope])
    #plt.axis([-1.0, 1.0, -1, 1])

n = 1000
runs = 1000
errors = 0
averageWeight = np.zeros([6,])
for i in range(runs):
    #samples = [[random.uniform(-1, 1) for i in range(2)] for i in range(2)]
    points = GeneratePoints(n)
    points = NonLinearClassify(points)
    #plt.scatter(points[:, [5]], points[:, [6]], c=points[:, [7]])
    #plt.show()
    matrixX = points[:,0:6]
    vectorY = points[:, 6]
    squareMatrix = np.dot(np.transpose(matrixX), matrixX)
    squareMatrixInverse = np.linalg.inv(squareMatrix)
    pseudoInverse = np.dot(squareMatrixInverse, np.transpose(matrixX))
    weight = np.dot(pseudoInverse, vectorY)
    averageWeight += weight
    for point in points:
        hypo = Hypothesis(weight, point)
        if hypo != point[6]:
            errors += 1


    """"PLA
  errorList = list()
  for j in range(maxIters):
      for point in points:
          hypo = Hypothesis(weight, point)
          if (hypo != point[3]):
              errorList.append(point)
      if len(errorList) > 0:
          errPoint = random.choice(errorList)
          weight = UpdateWeight(weight, errPoint)
  # check training
  for point in points:
      hypo = Hypothesis(weight, point)
      if (hypo != point[3]):
          errors += 1
          """


print("Average weight vector is: %s" % (averageWeight / runs))
outErrors = 0
for i in range(runs):
    points = GeneratePoints(n)
    points = NonLinearClassify(points)
    for point in points:
        hypo = Hypothesis(averageWeight, point)
        if hypo != point[6]:
            outErrors += 1

averageErrors = (errors / runs) / n
averageOutErrors = (outErrors / runs) / n
print("Total average errors by the learning from data: %s" % (averageErrors))
print("Total average errors by the learning from data: %s" % (averageOutErrors))


