import math
class rational():
    def __init__(self, a=0, b=1):
        self.nominator = int(a)
        self.denominator = int(b)

    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)

    def __add__(self, other):
        return self.add(other)

    def add(self, b):
        return rational((b.denominator*self.nominator) + (self.denominator * b.nominator), b.denominator * self.denominator )

    def __sub__(self, other):
        return self.sub(other)

    def sub(self, b):
        return rational((self.nominator * b.denominator) - (self.denominator * b.nominator), self.denominator * b.denominator)

    def __mul__(self, other):
        return self.mul(other)

    def mul(self, b):
        return rational(self.nominator * b.nominator, self.denominator * b.denominator)

    def __truediv__(self, other):
        return self.truediv(other)

    def truediv(self, b):
        return rational(self.nominator * b.denominator, self.denominator * b.nominator )

    def __int__(self):
        return int(self.nominator / self.denominator)

    def __float__(self):
        return float(self. nominator / self.denominator)

    def gt(self, other):
        if float(self) > float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        return self.gt(other)

    def lt(self, other):
        if float(self) < float(other):
            return True
        else:
            return False

    def __lt__(self, other):
        return self.lt(other)

    def eq(self, other):
        if float(self) == float(other):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.eq(other)

    def simplify(self):
        greatest = max(self.nominator, self.denominator)
        lowest = min(self.nominator, self.denominator)
        if lowest == 0:
            return greatest
        remainder = (greatest % lowest)
        return rational(lowest, remainder).simplify()

    def rationalToInt(self):
        if self.nominator % self.denominator == 0:
            return int(self.nominator / self.denominator)
        else:
            return self
class vector():
    def __init__(self, n, scalar = 0):
        self.length = n
        if type(scalar) == float or type(scalar) == int:
            self.v = [float(scalar) for x in range(self.length)]
        if type(scalar) == rational:
            self.v = [float(scalar.nominator / scalar.denominator) for x in range(self.length)]
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
class function():
    def eval(self, x):
        return self.eval(x)
    def lincomb(self, g, alpha, beta):
        return self.lincomb(g, alpha, beta)
    def scalar(self, alpha):
        return self.scalar(self, alpha)
    def multiply(self, g):
        return self.multiply(self, g)
    def divide(self, g):
        return self.divide(self, g)
    def inner(self, g):
        return self.inner(self, g)
    def norm(self):
        return self.norm(self)
    def diff(self, n):
        return self.diff(self, n)
    def __add__(self, other):
        return self.add(other)
    def add(self, other):
        return self.add(other)
    def __sub__(self, other):
        return self.sub(other)
    def sub(self, other):
        return self.sub(other)
    def __mul__(self, other):
        return self.mul(other)
    def mul(self, other):
        return self.mul(other)
    def __truediv__(self, other):
        return self.truediv(other)
    def truediv(self, other):
        return self.truediv(other)
class polynomial(function):
    def __init__(self, vec):
        self.coefficients = vector(len(vec), vec)
    def eval(self, x):
        result = 0.0
        for i in range(0, len(self.coefficients.v)):
            result += self.coefficients.v[i] * (x**i)
        return result
    def lincomb(self, g, alpha, beta):
        self.scalar(alpha)
        g.scalar(beta)
        return polynomial(self.coefficients.add(g.coefficients).v)
    def scalar(self, alpha):
        self.coefficients = self.coefficients.scalar(alpha)
        return self
    def multiply(self, g):
        selfLen, gLen = len(self.coefficients.v), len(g.coefficients.v)
        newLen = selfLen + gLen - 1
        result = [0 for i in range(newLen)]
        for i in range(0, selfLen):
            for j in range(0, gLen):
                result[i + j] += self.coefficients.v[i] * g.coefficients.v[j]
        return polynomial(result)
    def inner(self, g):
        polyMul = self.multiply(g)
        polyMulLen = len(polyMul.coefficients.v)
        result = [0 for i in range(polyMulLen + 1)]
        for i in range(0, len(result)):
            if i == 1:
                result[i] = polyMul.coefficients.v[i - 1]
            if i > 1:
                result[i] = polyMul.coefficients.v[i - 1] / i
        return sum(result)
    def norm(self):
        newFunction = self.inner(self)
        return newFunction**0.5
    def diff(self, n):
        if n < len(self.coefficients.v):
            polyLen = len(self.coefficients.v)
            result = [0 for i in range(polyLen)]
            while n > 0:
                for i in range(0, polyLen - 1):
                    result[i] = self.coefficients.v[i + 1] * (i + 1)
                self.coefficients.v = result
                n -= 1
                i = 0

            poly = polynomial(result)
            return poly
        if n >= len(self.coefficients.v):
            return polynomial([0])
    def add(self, other):
        return polynomial(self.coefficients.add(other.coefficients).v)
    def sub(self, other):
        return polynomial(self.coefficients.sub(other.coefficients).v)
    def rootNewton(self, guess, tolerance):
        difference = 1
        poly = polynomial(self.coefficients.v)
        polyDiff = polynomial(self.diff(1).coefficients.v)
        while difference > tolerance:
            evalPoly = poly.eval(guess)
            evalPolyDiff = polyDiff.eval(guess)
            result = guess - (evalPoly / evalPolyDiff)
            difference = abs(result - guess)
            guess = result
        return guess
    def rootNewtonSecond(self, guess, tolerance):
        if self.coefficients.v[0] == 0:
            return 0
        difference = 1
        polyDiff = polynomial(self.diff(1).coefficients.v)
        while difference > tolerance:
            evalPoly = poly.eval(guess)
            evalPolyDiff = polyDiff.eval(guess)
            result = guess - (evalPoly / evalPolyDiff)
            difference = abs(result - guess)
            guess = result
        return guess
    def rootLaguerre(self, guess, tolerance):
        result = 1
        denominator = 1
        poly = polynomial(self.coefficients.v)
        n = len(poly.coefficients.v) - 1
        polyDiff = polynomial(self.diff(1).coefficients.v)
        polyDiffDiff = polynomial(self.diff(2).coefficients.v)
        while abs(result) > tolerance and n >= 2:
            evalPoly = poly.eval(guess)
            evalPolyDiff = polyDiff.eval(guess)
            evalPolyDiffDiff = polyDiffDiff.eval(guess)
            G = evalPolyDiff / evalPoly
            H = G**2 -  (evalPolyDiffDiff / evalPoly)
            denominatorPLus = G + (((n-1)*(n*H - G**2))**0.5)
            denominatorMin = G - (((n-1)*(n*H - G**2))**0.5)
            if abs(denominatorPLus) > abs(denominatorMin):
                denominator = denominatorPLus
            if abs(denominatorPLus) < abs(denominatorMin):
                denominator = denominatorMin
            result = n / denominator
            guess = guess - result
        while abs(result) > tolerance and n == 1:
            poly.coefficients.v[0] = (poly.coefficients.v[0] / poly.coefficients.v[1]) * -1
            return poly.coefficients.v[0]
        return guess
class fourierseries(function):
    def __init__(self, vectorFirst, vectorSecond):
        self.cosCoefficients = vectorFirst
        self.sinCoefficients = vectorSecond
    def eval(self, x):
        summation = 0
        for k in range(1, len(self.cosCoefficients)):
            summation += math.cos(2 * k * math.pi * x) + math.sin(2 * k * math.pi * x)
        return summation + self.cosCoefficients[0]
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







