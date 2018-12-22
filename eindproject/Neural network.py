import csv
import pandas
from pandas.tools.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt


m = 150
label = {"Iris-setosa" : 1, "Iris-versicolor" : 2, "Iris-virginica" : 3}
X = np.zeros((150,4))
y = np.zeros(m)

with open('Iris.csv', newline='') as csvfile:
	     reader = csv.reader(csvfile, delimiter=',')
	     # skip headers
	     print(next(reader, None))
	     # loop over rows
	     for row in reader:
	     	# index
	     	k = int(row[0])-1
	     	# features
	     	X[k,:] = row[1:5]
	     	# labels
	     	y[k] = label[row[5]]

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# info over de datatset
#print(X.shape)
#print(dataset.head(20))
#print(dataset.describe())
#print(dataset.groupby("class").size())


# box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()
#dataset.hist()
#plt.show()
#scatter_matrix(dataset)
#plt.show()

# sigmoid functie
def sigmoid(x):
    return 1/(1+np.exp(-x))


# misfit functie
def misfit(p):
    yt = sigmoid(np.dot(X, p[:-1]) + p[-1])
    residual = yt - y
    return residual**2

# gradient
def gradient(p):
    s = np.dot(X, p[:-1]) + p[-1]
    yt = sigmoid(s)
    g = np.zeros(len(p))
    g[:-1] = 2 * np.dot(np.transpose(X) * sigmoid(s) * (1 - sigmoid(s)) * (yt - y), np.ones(len(yt)))
    g[-1] = 2 * np.dot(sigmoid(s) * (1 - sigmoid(s)) * (yt - y), np.ones(len(yt)))
    return g


# invoer voor OF operatie
"""X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])"""

"""# uitvoer
y = np.array([0, 0, 0, 1])"""


"""plt.scatter(X[0:51], X[0:51], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()"""

# beginschatting voor de gewichten
p = np.array([0, 0, 0, 0, 0])

# doe aan aantal iteraties
alpha = 1e1  # stapgrootte, kies deze zodat f steeds kleiner wordt
for iter in range(200):
    f = misfit(p)
    g = gradient(p)
    p = p - alpha * g

    print(iter, f, np.dot(g, g))

print('Weights               : ', p)
print('Training data         : ', y)
print('Output After Training : ', sigmoid(np.dot(X, p[:-1]) + p[-1]))

