import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import queue
class Feature(object):
    def __init__(self, name, options):
        self.name = name
        self.options = options
class Node(object):
    def __init__(self, feature = None, category = []):
        self.category = list(category)
        # leaf node, category contains only one kind of class
        if self.entropy() == 0:
            self.name = self.category[0]
        else:
            self.name = feature.name
        self.children = {}
        if feature.options is not None:
            for option in feature.options:
                self.addNode(option)

    def __repr__(self):
        return self.name

    def addNode(self, option):
        #TODO
        categories = query(self.name, option)
        node = Node(Feature("Not defined", []), categories)
        self.children[option] = node

    def entropy(self):
        sums = [0,0,0,0]
        totalItems = len(self.category)
        for item in self.category:
            if item == "unacc":
                sums[0] += 1
            elif item == "acc":
                sums[1] += 1
            elif item == "good":
                sums[2] += 1
            elif item == "v-good":
                sums[3] += 1
        result = 0
        for sum in sums:
            probability = sum / totalItems
            if probability == 0 or probability == 1: continue;
            else:
                result += probability * math.log2(probability)
        return -(result)

def options(series):
    result = list()
    for item in series:
        if item not in result:
            result.append(item)
    return result

def query(featureName, featureOption):
    # TODO
    condition = data[featureName] == featureOption
    result = data[condition]["category"]
    return result

def findNode(tree):
    q = queue.Queue()
    q._put(tree)
    while q.empty() == False:
        node = q.get()
        if node.name == "Not defined":
            return node
        for child in node.children:
            q.put(node.children[child])

def getBestFeature(features, categories):
    highestGain = 0
    bestFeature = Feature("", [])
    featureTest = queue.Queue()
    for feature in features:
        featureTest._put(feature)

    while featureTest.empty() == False:
        feature = featureTest.get()
        #TODO
        node = Node(feature, categories)
        entropyBefore = node.entropy()
        totalBefore = len(node.category)
        entropyAfter = 0
        # calc average entropy among childs from feature
        for child in node.children:
            entropy = node.children[child].entropy()
            totalAfer = len(node.children[child].category)
            weight = totalAfer / totalBefore
            entropyAfter += entropy * weight
        gain = entropyBefore - entropyAfter
        print(feature.name + " gain: " + str(gain))
        if gain > highestGain:
            highestGain = gain
            bestFeature = feature

    return bestFeature

url = "C:/Users/lexme/OneDrive/Documenten/Auto.txt"
columns = ["buying", "maint", "doors", "persons", "lugBoot", "safety", "category"]
data = pd.read_csv(url, sep=",",nrows= 500)
data.columns = columns
features = list()
category = data["category"]

index = -1
for column in data:
    index += 1
    if index < data.shape[1] - 1:
        feature = Feature(column, options(data[column]))
        features.append(feature)





Tree = Node(Feature("Not defined", []), category)
bestFeature = getBestFeature(features, category)
features.remove(bestFeature)
Tree = Node(bestFeature, category)

for child in Tree.children:
    print(Tree.children[child].entropy())
    print(Tree.children[child].name)



















