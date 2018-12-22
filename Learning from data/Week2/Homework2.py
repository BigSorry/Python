import random
import sys

runs = 100000
totalFirstHeads = 0
totalRandomHeads = 0
totalMinHeads = 0
while runs > 0:
    coins = 1000
    randomCoin = random.randint(0, 1000)
    coinMinHeads = sys.maxsize
    while coins > 0:
        currentHeads = 0
        for i in range(10):
            flip = random.randint(0,1)
            if flip == 1:
                # a 1 is a coin flip heads
                currentHeads += 1
        if coins == 1000:
            totalFirstHeads += currentHeads
        if coins == randomCoin:
            totalRandomHeads += currentHeads
        if currentHeads < coinMinHeads:
            coinMinHeads = currentHeads
        coins -= 1
    totalMinHeads += coinMinHeads
    runs -= 1



print(totalFirstHeads / 100000)
print(totalRandomHeads / 100000)
print("The average value of Vmin is close to: %s" % (totalMinHeads / 100000))