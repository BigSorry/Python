def NestedSum(integers):
    list = []
    sum = 0
    for x in range(len(integers)):
        list += integers[x]

    for i in list:
        sum += i

    return sum
def CumSum(numbers):
    list = numbers
    cum = 0
    for i in range(len(numbers)):
        cum += numbers[i]
    list.pop(1)
    list.append(cum)
    return list
def Middle(list):
    list2 = list
    list2.pop(len(list)-1)
    list2.pop(0)
    return list2
def Chop(list):
    del list[len(list)-1]
    del list[0]
    return list
def IsSorted(list):
    t = sorted(list)
    if t == list:
        return True
    else:
        return False
def IsAnagram(str1, str2):
    sum = 0
    list1 = list(str1)
    list2 = list(str2)
    while len(list1) == len(list2):
        for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[j] == list2[i]:
                        sum+=1

        if sum == len(list1):
            return True
        else:
            return False
    else:
        print("Strings are not equal length")
def HasDuplicates(list):
    for x in range(len(list)):
        for y in range(len(list)):
            if list[x] == list[y] and x!=y:
                return True
    else:
        return False

t = [1, 3, 2, 1, 2]
bool = HasDuplicates(t)
print(bool)




