import math

class vector():
    def __init__(self, n, scalar = 0):
        self.length = n
        if type(scalar) == float or type(scalar) == int:
            self.v = [float(scalar) for x in range(self.length)]
        if type(scalar) == list:
            self.v = [float(scalar[x]) for x in range(self.length)]
    """"def __str__(self):
        result = ""
        for x in range(self.length):
            result += str(self.v[x]) + "\n"
        return result"""
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
    def __sub__(self, other):
        return self.sub(other)
    def sub(self, other):
        if self.length == other.length:
            array = [0 for x in range(len(self.v))]
            for x in range(self.length):
                array[x] = self.v[x] - other.v[x]
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
class fourierseries():
    def __init__(self, vectorFirst, vectorSecond):
        self.cosCoefficients = vector(len(vectorFirst), vectorFirst)
        self.sinCoefficients = vector(len(vectorSecond), vectorSecond)
    def eval(self, x):
        summation = 0
        for k in range(0, len(self.cosCoefficients.v)):
            summation += (
                (math.cos(2 * k * math.pi * x) + math.sin(2 * k * math.pi * x)) *
            (math.cos(2 * k * math.pi * x) + math.sin(2 * k * math.pi * x))
            )

        return summation
    def lincomb(self, g, alpha, beta):
        newSelf = self.scalar(alpha)
        newG = g.scalar(beta)
        resultCos = newSelf.cosCoefficients.add(newG.cosCoefficients)
        resultSin = newSelf.sinCoefficients.add(newG.sinCoefficients)
        return fourierseries(resultCos, resultSin)
    def scalar(self, alpha):
        self.cosCoefficients = self.cosCoefficients.scalar(alpha)
        self.sinCoefficients = self.sinCoefficients.scalar(alpha)
        return self
    def add(self, other):
       return fourierseries(self.cosCoefficients.add(other.cosCoefficients),
        self.sinCoefficients.add(other.sinCoefficients))
    def sub(self, other):
       return fourierseries(self.cosCoefficients.sub(other.cosCoefficients),
        self.sinCoefficients.sub(other.sinCoefficients))
    def IntegralF(self):
        n = len(self.cosCoefficients.v)
        result = 0
        for k in range(0, n):
            if k == 0:
                result += self.cosCoefficients.v[0]**2
            if k != 0:
                result += (
                (4*math.pi*k)*(self.cosCoefficients.v[k]**2 + self.sinCoefficients.v[k]**2) +
                (self.cosCoefficients.v[k] - self.sinCoefficients.v[k])*(self.cosCoefficients.v[k]+self.sinCoefficients.v[k])*math.sin(4*math.pi*k)-
                2*self.cosCoefficients.v[k]*self.sinCoefficients.v[k]*math.cos(4*math.pi * k) +
                2*self.cosCoefficients.v[k] * self.sinCoefficients.v[k]
            ) / (8*math.pi *k)
        return result
    def IntegralFDiff(self):
        n = len(self.cosCoefficients.v)
        result = 0
        for k in range(0, n):
            result += (
                         (4 * math.pi * k) * (self.cosCoefficients.v[k] ** 2 + self.sinCoefficients.v[k] ** 2) +
                         (self.cosCoefficients.v[k] - self.sinCoefficients.v[k]) * (
                         self.cosCoefficients.v[k] + self.sinCoefficients.v[k]) * math.sin(4 * math.pi * k) -
                         2 * self.cosCoefficients.v[k] * self.sinCoefficients.v[k] * math.cos(4 * math.pi * k) +
                         2 * self.cosCoefficients.v[k] * self.sinCoefficients.v[k]
                     ) * ((math.pi*k) / 2)
        return result


inputCoef = [float(a) for a in input().split()]
inputCoefSecond = [float(a) for a in input().split()]

#inputCoefSecond[0] = inputCoef[0]
series2 = fourierseries(inputCoef, inputCoefSecond)
series = fourierseries(inputCoef, inputCoefSecond)


num = series.IntegralFDiff()
denum = series2.IntegralF()
result = (num / denum)**0.5
print("{:.2f}".format(result))
