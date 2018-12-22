import math
class node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
def preorderRead(tree, lijst):
    if tree != None:
        lijst.append(tree.value)
        preorderRead(tree.left, lijst)
        preorderRead(tree.right, lijst)
def preorderFill(lijst, tree):
    if tree != None:
        tree.value = lijst[0]
        lijst.pop(0)
        preorderFill(lijst, tree.left)
        preorderFill(lijst, tree.right)
def CreateTree(tree, nodes):
    if tree != None and nodes > 0:
        tree.left = node()
        tree.right = node()
        CreateTree(tree.left, nodes - 1)
        CreateTree(tree.right, nodes -1)
def getBinaryTree(n):
    Tree = node()
    CreateTree(Tree, n)
    return Tree
def inorderFill(lijst, tree):
    if tree != None:
        inorderFill(lijst, tree.left)
        tree.value = lijst[0]
        lijst.pop(0)
        inorderFill(lijst, tree.right)
def sumRead(tree, numberLijst, routeLijst):
    if tree != None:
        numberLijst.append(tree.value)
        if routeLijst != []:
            step = routeLijst[0]
            if step == "L":
                routeLijst.pop(0)
                sumRead(tree.left, numberLijst, routeLijst)
            if step == "R":
                routeLijst.pop(0)
                sumRead(tree.right, numberLijst, routeLijst)

numberList = [int(a) for a in input().split()]
routeList = list(input())
h = math.log2(len(numberList) + 1) - 1
Tree = getBinaryTree(h)
inorderFill(numberList, Tree)
sumRead(Tree, numberList, routeList)
sum = 0
for i in range(0, len(numberList)):
    sum += numberList[i]
print(sum)



