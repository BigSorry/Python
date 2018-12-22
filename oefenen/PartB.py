import math
class vector():
    def __init__(self, n, scalar = 0):
        self.length = n
        if type(scalar) == float or type(scalar) == int:
            self.v = [float(scalar) for x in range(self.length)]
        else:
            self.v = [float(scalar[x])for x in range(self.length)]
        """"if type(scalar) == rational:
            self.v = [float(scalar.nominator / scalar.denominator) for x in range(self.length)]"""
    def __str__(self):
        result = ""
        for x in range(self.length):
            result += str(self.v[x]) + "\n"
        return result
    def __add__(self, other):
        return self.add(other)
    def add(self, other):
        if self.length == other.length:
            array = [0 for x in range(len(self.v))]
            for x in range(self.length):
                array[x] = self.v[x] + other.v[x]
            return vector(self.length, array)
        else:
            return print("vectors need to be the same length")
    def __mul__(self, other):
        return self.mul(other)
    def mul(self, other):
        if self.length == other.length:
            return vector(self.length, [self.v[x] * other.v[x]for x in range(len(self.v))])
        else:
            return print("vectors need to be the same length")

    def linCombination(self, other, alpha, beta):
        vector1 = vector(self.length, [alpha * x for x in self.v])
        vector2 = vector(other.length, [beta * i for i in other.v])
        return vector1 + vector2
    def scalar(self, scalar):
        return vector(self.length, [scalar * x for x in self.v])
    def inner(self, other):
        vector = self * other
        sum = 0
        for x in vector.v:
            sum += x
        return sum
    def normalize(self):
        return (self.inner(self)**0.5)
    def gt(self, other):
        if self.normalize() > other.normalize():
            return True
        else:
            return False
    def __gt__(self, other):
        return self.gt(other)
    def lt(self, other):
        if self.normalize() < other.normalize():
            return True
        else:
            return False
    def __lt__(self, other):
        return self.lt(other)
    def eq(self, other):
        if self.normalize() == other.normalize():
            return True
        else:
            return False
    def __eq__(self, other):
        return self.eq(other)

inputFirst = [float(a) for a in input().split()]
inputSecond = [float(b) for b in input().split()]
vectorFirst = vector(len(inputFirst), inputFirst)
vectorSecond = vector(len(inputSecond), inputSecond)

dot = vectorFirst.inner(vectorSecond)
magnitudeFirst = vectorFirst.normalize()
magnitudeSecond = vectorSecond.normalize()
cos = dot / (magnitudeFirst * magnitudeSecond)
result = (math.acos(cos) * (180 / math.pi))
print("{:.2f}".format(result))
x = vector(3, 1)
print(x)