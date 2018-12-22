import math
def mysqrt(a):
    epsilon = 0.000001
    x = a - 1
    while True:
        y = (x + (a/x)) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return y
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
def estimate_pi(k):
    result = 0
    epsilon = 0.000001
    constant = (2 * math.sqrt(2)) / 9801
    while True and k < 200:
        nominator = factorial(4*k) * (1103 + (26390 * k))
        denominator = (factorial(k)**(4) ) * 396**(4*k)
        result += nominator / denominator
        k+=1
        final_result = result * constant
        if abs(math.pi - final_result) < epsilon:
           break

    return result * constant


