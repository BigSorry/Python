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
def printResult(string, rationalFirst, rationalSecond):
    result = 0
    if string == "+":
        result = rationalFirst + rationalSecond
    if string == "-":
        result = rationalFirst - rationalSecond
    if string == "*":
        result = rationalFirst * rationalSecond
    if string == "/":
        result = rationalFirst / rationalSecond

    gcd = result.simplify()
    print(rational(result.nominator / gcd, result.denominator / gcd).rationalToInt())

inputFirst = input().split("/")
inputSecond = input().split("/")
inputThird = input().split("'")

rationalFirst = rational(int(inputFirst[0]), int(inputFirst[1]))
rationalSecond = rational(int(inputSecond[0]), int(inputSecond[1]))

printResult(inputThird[0], rationalFirst, rationalSecond)