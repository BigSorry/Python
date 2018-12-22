import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import math
from sqlalchemy import create_engine
from itertools import chain, combinations
from sklearn.ensemble import RandomForestRegressor


def conditionalProb(trainingSet, columnNames):
    options = {}
    combinations = 1
    for i in columnNames:
        array = list()
        array.append(trainingSet[i].unique())
        array.append(len(trainingSet[i].unique()) - 1)
        options[i] = array
        combinations *= len(trainingSet[i].unique())

    combDict = {}
    while combinations > 0:
        change = 0
        combo = list()
        for key in options:
            index = options[key][1]
            combo.append(options[key][0][index])
        combDict[combinations] = combo

        columnIndex = len(columnNames) - 1
        while change >= 0:
            if options[columnNames[columnIndex]][1] == 0:
                options[columnNames[columnIndex]][1] = len(options[columnNames[columnIndex]][0]) - 1
                columnIndex -= 1
            else:
                options[columnNames[columnIndex]][1] -= 1
                change -= 1
        combinations -= 1

    output = list()
    for comboKey in combDict:
        query = ' & '.join(['{} == {}'.format(columnNames[i], combDict[comboKey][i]) for i in range(len(columnNames))])
        spaceRows = trainingSet.query(query)
        space = spaceRows.shape[0]
        if space == 0:
            continue
        else:
            survivors = spaceRows.loc[spaceRows.Survived == 1, "Survived"].shape[0]
            array = list()
            columns = combDict[comboKey]
            probAlive = (survivors / space)
            array.append(columns)
            array.append(probAlive)
            output.append(array)
    return output

def getTitle(name):
    title = re.search(' ([A-Za-z]+)\.', name)
    if title:
        return title.group(1)
    else:
        return ""

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

path = "C:/Users/lexme/Downloads/train.csv"
path2 = "C:/Users/lexme/Downloads/test.csv"
trainData = pd.read_csv(path)
testData = pd.read_csv(path2)
testData['Survived'] = -1
fullData = trainData.append(testData)
print(trainData.columns)

# make class based on familysize
fullData["FamilySize"] = fullData["Parch"] + fullData["SibSp"] + 1
fullData.loc[fullData["FamilySize"] == 1, "FamilyClass"] = 0
fullData.loc[(fullData["FamilySize"] >= 2) & (fullData["FamilySize"] <= 4), "FamilyClass"] = 1
fullData.loc[fullData["FamilySize"] >= 5, "FamilyClass"] = 2
fullData['FamilyClass'] = fullData['FamilyClass'].astype(int)

# makes titles based on name
fullData["Title"] = fullData["Name"].apply(getTitle)
fullData['Title'] = fullData['Title'].replace('Mlle', 'Miss')
fullData['Title'] = fullData['Title'].replace('Ms', 'Miss')
fullData['Title'] = fullData['Title'].replace('Mme', 'Mrs')
fullData['Title'] = fullData['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

#integer titles
fullData.loc[fullData['Title'] == "Master", 'Title'] = 1
fullData.loc[fullData['Title'] == "Miss", 'Title'] = 2
fullData.loc[fullData['Title'] == "Mr", 'Title'] = 3
fullData.loc[fullData['Title'] == "Mrs", 'Title'] = 4
fullData.loc[fullData['Title'] == "Rare", 'Title'] = 5

# Mapping Fare
# one null value
fullData.loc[fullData.Fare.isnull() == True, "Fare"] = 1
fullData.loc[fullData['Fare'] <= 7.91, 'Fare'] = 0
fullData.loc[(fullData['Fare'] > 7.91) & (fullData['Fare'] <= 14.454), 'Fare'] = 1
fullData.loc[(fullData['Fare'] > 14.454) & (fullData['Fare'] <= 31), 'Fare']  = 2
fullData.loc[fullData['Fare'] > 31, 'Fare']  = 3
fullData['Fare'] = fullData['Fare'].astype(int)

#sex
fullData.loc[fullData['Sex'] == "male", 'Sex'] = 0
fullData.loc[fullData['Sex'] == "female", 'Sex'] = 1

#fill missing age with randomForest
trainFeatures = fullData.loc[fullData.Age.notna() == True, ["Title","Sex" , "FamilyClass", "Pclass"]]
trainLabels = fullData.loc[fullData.Age.notna() == True, "Age"]
testFeatures = fullData.loc[fullData.Age.notna() == False, ["Title","Sex" , "FamilyClass", "Pclass"]]
randomForest = RandomForestRegressor(n_estimators=100,
                                max_depth=5,
                                min_samples_split=10,
                                min_samples_leaf=5,
                                random_state=0)
randomForest.fit(trainFeatures, trainLabels)
prediction = randomForest.predict(testFeatures)
fullData.loc[fullData.Age.notna() == False, "Age"] = prediction

#integer class age
fullData.loc[fullData['Age'] <= 16, 'Age'] = 0
fullData.loc[(fullData['Age'] > 16) & (fullData['Age'] <= 32), 'Age'] = 1
fullData.loc[(fullData['Age'] > 32) & (fullData['Age'] <= 48), 'Age'] = 2
fullData.loc[(fullData['Age'] > 48) & (fullData['Age'] <= 64), 'Age'] = 3
fullData.loc[fullData['Age'] > 64, 'Age'] = 4

trainData = fullData.loc[fullData.Survived != -1, :]
testData = fullData.loc[fullData.Survived == -1,:]
columnArray = list(["Sex" , "FamilyClass","Title", "Pclass","Fare",  "Age"])
allProbs = {}
choose = len(columnArray)
powerSet = list(powerset(columnArray))

for set in powerSet:
    if set == tuple(""):
        #empty set
        continue
    probs = conditionalProb(trainData, set)
    for array in probs:
        columnValues = tuple(array[0])
        prob = array[1]
        print("the columns are {0} and the prob is {1} \n".format(str(columnValues), prob))
        key = set + columnValues
        print(key)
        allProbs[key] = prob
    #columnArray.pop()

columnArray = list(["Sex" , "FamilyClass","Title", "Pclass","Fare",  "Age"])
# dont forget to iter through testData
for index, row in testData.iterrows():
    rowKey = tuple(columnArray) + tuple(row.loc[columnArray])
    if rowKey in allProbs:
        if allProbs[rowKey] >= 0.75:
            #trainData.loc[index, "Validate"] = 1
            testData.loc[index, "Survived"] = 1
        elif allProbs[rowKey] <= 0.25:
            #trainData.loc[index, "Validate"] = 0
            testData.loc[index, "Survived"] = 0
        else:
            #trainData.loc[index, "Validate"] = -1
            testData.loc[index, "Survived"] = -1
            print("not classed ",rowKey, "With prob ", allProbs[rowKey])

#file output for kaggle
missed = testData.loc[testData.Survived == -1].shape[0]
while missed > 0 and len(columnArray) > 0:
    missed = testData.loc[testData.Survived == -1].shape[0]
    print("missed: ", missed, " len col ", len(columnArray))
    columnArray.pop()
    for index, row in testData.iterrows():
        if row.Survived != -1:
            continue
        else:
            rowKey = tuple(columnArray) + tuple(row.loc[columnArray])
            if rowKey in allProbs:
                if allProbs[rowKey] >= 0.8:
                    #trainData.loc[index, "Validate"] = 1
                    testData.loc[index, "Survived"] = 1
                elif allProbs[rowKey] <= 0.2:
                    #trainData.loc[index, "Validate"] = 0
                    testData.loc[index, "Survived"] = 0
                else:
                    #trainData.loc[index, "Validate"] = -1
                    testData.loc[index, "Validate"] = -1
                    print("not classed ", rowKey, "With prob ", allProbs[rowKey])

"""
print(missed)
trainData.loc[(trainData.Validate == -1) & (trainData.Sex == 1), "Validate"] = 1
trainData.loc[(trainData.Validate == -1) & (trainData.Sex == 2), "Validate"] = 0
predictRate = (trainData.loc[:, "Survived"] == trainData.loc[:, "Validate"])
trues = np.sum(predictRate)
print("In sample prediction rate ", (trues / trainData.shape[0]))

"""

testData.loc[(testData.Survived == -1) & (testData.Sex == 1), "Survived"] = 1
testData.loc[(testData.Survived == -1) & (testData.Sex == 0), "Survived"] = 0
output = testData[["PassengerId", "Survived"]]
output.to_csv('OutputProb.csv', sep=',', index = False)



