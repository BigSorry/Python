import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
import re
def sign(numbers):
    index = 0
    for number in numbers:
        if number >= 0:
            numbers[index] =  1
        else:
            numbers[index] = 0
        index += 1
    return numbers
def getTitle(name):
    title = re.search(' ([A-Za-z]+)\.', name)
    if title:
        return title.group(1)
    else:
        return ""

path = "C:/Users/lexme/Downloads/train.csv"
path2 = "C:/Users/lexme/Downloads/test.csv"
trainData = pd.read_csv(path)
testData = pd.read_csv(path2)
fullData = [trainData, testData]
print(trainData.columns)

# make class based on familysize
trainData["FamilySize"] = trainData["Parch"] + trainData["SibSp"] + 1
trainData.loc[trainData["FamilySize"] == 1, "FamilyClass"] = 1
trainData.loc[(trainData["FamilySize"] >= 2) & (trainData["FamilySize"] <= 4), "FamilyClass"] = 2
trainData.loc[trainData["FamilySize"] >= 5, "FamilyClass"] = 3
trainData['FamilyClass'] = trainData['FamilyClass'].astype(int)

testData["FamilySize"] = testData["Parch"] + testData["SibSp"] + 1
testData.loc[testData["FamilySize"] == 1, "FamilyClass"] = 1
testData.loc[(testData["FamilySize"] >= 2) & (testData["FamilySize"] <= 4), "FamilyClass"] = 2
testData.loc[testData["FamilySize"] >= 5, "FamilyClass"] = 3
testData['FamilyClass'] = testData['FamilyClass'].astype(int)

# makes titles based on name
trainData["Title"] = trainData["Name"].apply(getTitle)
trainData['Title'] = trainData['Title'].replace('Mlle', 'Miss')
trainData['Title'] = trainData['Title'].replace('Ms', 'Miss')
trainData['Title'] = trainData['Title'].replace('Mme', 'Mrs')
trainData['Title'] = trainData['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

testData["Title"] = testData["Name"].apply(getTitle)
testData['Title'] = testData['Title'].replace('Mlle', 'Miss')
testData['Title'] = testData['Title'].replace('Ms', 'Miss')
testData['Title'] = testData['Title'].replace('Mme', 'Mrs')
testData['Title'] = testData['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

# Mapping Fare
trainData.loc[trainData['Fare'] <= 7.91, 'Fare'] = 1
trainData.loc[(trainData['Fare'] > 7.91) & (trainData['Fare'] <= 14.454), 'Fare'] = 2
trainData.loc[(trainData['Fare'] > 14.454) & (trainData['Fare'] <= 31), 'Fare']  = 3
trainData.loc[ trainData['Fare'] > 31, 'Fare']  = 4
trainData['Fare'] = trainData['Fare'].astype(int)


testData.loc[testData['Fare'] <= 7.91, 'Fare'] = 1
testData.loc[(testData['Fare'] > 7.91) & (testData['Fare'] <= 14.454), 'Fare'] = 2
testData.loc[(testData['Fare'] > 14.454) & (testData['Fare'] <= 31), 'Fare'] = 3
testData.loc[ testData['Fare'] > 31, 'Fare'] = 4
# one null value
testData.loc[testData.Fare.isnull() == True, "Fare"] = 1
testData['Fare' ] = testData['Fare'].astype(int)


#fill missing age
trainData.loc[trainData['Title'] == "Master", 'Age'] = 1
trainData.loc[trainData['Title'] == "Miss", 'Age'] = 0
trainData.loc[trainData['Title'] == "Mr", 'Age'] = 1
trainData.loc[trainData['Title'] == "Mrs", 'Age'] = 2
trainData.loc[trainData['Title'] == "Rare", 'Age'] = 2

testData.loc[testData['Title'] == "Master", 'Age'] = 1
testData.loc[testData['Title'] == "Miss", 'Age'] = 0
testData.loc[testData['Title'] == "Mr", 'Age'] = 1
testData.loc[testData['Title'] == "Mrs", 'Age'] = 2
testData.loc[testData['Title'] == "Rare", 'Age'] = 2

#numerical titles
trainData.loc[trainData['Title'] == "Master", 'Title'] = 1
trainData.loc[trainData['Title'] == "Miss", 'Title'] = 2
trainData.loc[trainData['Title'] == "Mr", 'Title'] = 3
trainData.loc[trainData['Title'] == "Mrs", 'Title'] = 4
trainData.loc[trainData['Title'] == "Rare", 'Title'] = 5

testData.loc[testData['Title'] == "Master", 'Title'] = 1
testData.loc[testData['Title'] == "Miss", 'Title'] = 2
testData.loc[testData['Title'] == "Mr", 'Title'] = 3
testData.loc[testData['Title'] == "Mrs", 'Title'] = 4
testData.loc[testData['Title'] == "Rare", 'Title'] = 5

#sex
trainData.loc[trainData['Sex'] == "male", 'Sex'] = 1
trainData.loc[trainData['Sex'] == "female", 'Sex'] = 2

testData.loc[testData['Sex'] == "male", 'Sex'] = 1
testData.loc[testData['Sex'] == "female", 'Sex'] = 2

#embarked
testData.loc[testData['Embarked'] == "S", 'Embarked'] = 1
testData.loc[testData['Embarked'] == "C", 'Embarked'] = 2
testData.loc[testData['Embarked'] == "Q", 'Embarked'] = 3

trainData.loc[trainData['Embarked'] == "S", 'Embarked'] = 1
trainData.loc[trainData['Embarked'] == "C", 'Embarked'] = 2
trainData.loc[trainData['Embarked'] == "Q", 'Embarked'] = 3


columnArray = list(["Title", "Age", "Sex", "Fare", "FamilyClass", "Pclass"])
print(trainData.Embarked.value_counts())
print(trainData.loc[:, columnArray].head())


matrixX = trainData.loc[:, columnArray].values
squareMatrix = np.dot(np.transpose(matrixX), matrixX)
inverseSquareMatrix = np.linalg.inv(squareMatrix)
pseudoMatrix =  np.dot(inverseSquareMatrix, np.transpose(matrixX))
weight = np.dot(pseudoMatrix, trainData.loc[:, "Survived"])
print(weight)
y = trainData.loc[:, "Survived"]

threshold = 0.5
bestThreshold = -100
maxTrue = -1
while threshold < 0.55:
    trainData["Test"] = sign(np.dot(matrixX, weight) - threshold)
    predictRate = (trainData.loc[:, "Survived"] == trainData.loc[:, "Test"])
    trues = np.sum(predictRate)
    if maxTrue < trues:
        maxTrue = trues
        bestThreshold = threshold
    threshold += 0.00001

print(bestThreshold)

testMatrix = testData.loc[:, columnArray].values
testData['Survived'] = sign(np.dot(testMatrix, weight) - bestThreshold)
output = testData[["PassengerId", "Survived"]]
output.to_csv('Output .csv', sep=',', index = False)

