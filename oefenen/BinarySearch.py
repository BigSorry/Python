list = [int(a) for a in input().split()]
b = int(input())

def BinarySearch(lijst, target):
    lowerIndex = 0
    upperIndex = len(lijst) - 1
    if lijst[upperIndex] == target and lijst[upperIndex -1] != lijst[upperIndex]:
        return upperIndex
    if lijst[lowerIndex] == target:
        return lowerIndex
    count = 0
    while count < len(lijst):
        count+=1
        midpoint = int((lowerIndex + upperIndex) / 2)
        if lijst[midpoint] == target and lijst[midpoint] != lijst[midpoint - 1]:
            return midpoint
        if target <= lijst[midpoint]:
            upperIndex = midpoint
        else:
            lowerIndex = midpoint
    else:
        return -1

print(BinarySearch(list, b))