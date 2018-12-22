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
        if float(self.nominator / self.denominator) > float(other.nominator / other.denominator):
            return True
        else:
            return False
    def __gt__(self, other):
        return self.gt(other)
    def lt(self, other):
        if float(self.nominator / self.denominator) < float(other.nominator / other.denominator):
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
        if self.nominator < 0 and self.denominator < 0:
            self.nominator *= -1
            self.denominator *= -1
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
class polynomial():
    def __init__(self, vec):
        self.coefficients = vector(len(vec), vec)
    def eval(self, x):
        result = rational(self.coefficients.v[0], 1)
        if type(x) == rational:
            for i in range(1, len(self.coefficients.v)):
                if self.coefficients.v[i] == 0.0:
                    continue
                addRat = rational(self.coefficients.v[i] * x.nominator**i , x.denominator**i)
                result =  result.add(addRat)
            return result
        """if type(x) != rational:
            result = 0.0
            for i in range(0, len(self.coefficients.v)):
                result += self.coefficients.v[i] * (x**i)
            return result"""
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

            return result
        if n > len(self.coefficients.v):
            return polynomial([0])
    def add(self, other):
        return polynomial(self.coefficients.add(other.coefficients).v)
    def sub(self, other):
        return polynomial(self.coefficients.sub(other.coefficients).v)
    def rootNewton(self, guess, tolerance):
        result = rational(1,1)
        difference = rational(1,1)
        guessRational = rational(guess, 1)
        poly = polynomial(self.coefficients.v)
        polyDiff = polynomial(self.diff(1))
        threshold = abs(tolerance / 1)
        count = 0
        while count < 4:
            evalPoly = poly.eval(guessRational)
            evalPolyDiff = polyDiff.eval(guessRational)
            resultDividing = evalPoly.truediv(evalPolyDiff)
            resultSub= guessRational.sub(resultDividing)
            difference = resultSub.sub(guessRational)
            guessRational = resultSub
            count += 1
        return guessRational
    def rootLaguerre(self, guess, tolerance):
        guessRat = rational(guess, 1)
        count = 0
        result = rational(1, 1)
        denominator = rational(0, 0)
        poly = polynomial(self.coefficients.v)
        n = len(poly.coefficients.v) - 1
        polyDiff = polynomial(self.diff(1))
        poly2 = polynomial(poly.coefficients.v)
        polyDiffDiff = polynomial(poly2.diff(2))
        #print(poly.coefficients.v, polyDiff.coefficients.v, polyDiffDiff.coefficients.v)
        while count < 5: #abs(result.nominator / result.denominator) > abs(tolerance) and n >= 2:
            evalPoly = poly.eval(guessRat)
            evalPolyDiff = polyDiff.eval(guessRat)
            evalPolyDiffDiff = polyDiffDiff.eval(guessRat)
            #print(evalPoly, evalPolyDiff , evalPolyDiffDiff)
            G = evalPolyDiff.truediv(evalPoly)
            G2 = G.mul(G)
            H = G2.sub(evalPolyDiffDiff.truediv(evalPoly))
            #print(G, G2, H)
            nHG = H.mul(rational(n, 1)).sub(G2)
            newRat = rational(n-1,1).mul(nHG)
            rat = rational(math.floor(newRat.nominator**0.5), math.floor(newRat.denominator**0.5))
            #print(rat)
            denominatorPLus = G.add(rat)
            denominatorMin = G.sub(rat)
            #print(denominatorPLus, denominatorMin)

            if abs(denominatorPLus.nominator / denominatorPLus.denominator) > abs(denominatorMin.nominator / denominatorMin.denominator):
                denominator = denominatorPLus
            if abs(denominatorPLus.nominator / denominatorPLus.denominator) < abs(denominatorMin.nominator / denominatorMin.denominator):
                denominator = denominatorMin
            print(denominator)
            result = rational(n, 1).truediv(denominator)
            guessNext = guessRat.sub(result)
            print(guessNext)
            count += 1
            """while abs(result) > tolerance and n == 1:
            poly.coefficients.v[0] = (poly.coefficients.v[0] / poly.coefficients.v[1]) * -1
            return poly.coefficients.v[0]"""
        return guessNext


inputCoef = [int(a) for a in input().split()]
inputGuess = int(input())
inputTolerance = [float(b) for b in input().split("e")]
tolerance = (inputTolerance[0]*10) * 10**inputTolerance[1]

poly = polynomial(inputCoef)

rationalBig = poly.rootNewton(inputGuess, tolerance)
gcd = rationalBig.simplify()
rationalBig.nominator = int(rationalBig.nominator / gcd)
rationalBig.denominator = int(rationalBig.denominator / gcd)
print(rationalBig)

