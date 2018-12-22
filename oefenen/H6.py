import math
def b(z):
    prod = a(z,z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x ,y, z):
    total = x + y + z
    square = b(total)**2
    return square
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
def ack(m,n):
    if m == 0:
        return n + 1
    if n == 0 and m > 0:
        return ack(m-1,1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    if first(word) == last(word) and len(word) > 2:
        return is_palindrome(middle(word))
    if len(word) <= 1:
        return True
    if len(word) == 2 and first(word) == last(word):
        return True
    else:
        return False
def is_power(a, b):
     if a > 0 and b > 0:
         if a % b == 0 and a % (a/b) == 0:
             return True
         else:
             return False
     else:
        return False
def GCD(a, b):
    if b > 0:
        biggest = max(a,b)
        smallest = min(a,b)
        remainder = biggest / smallest
        if biggest % smallest == 0 and biggest % (remainder) == 0 and  smallest % (remainder) == 0:
            return smallest
        else:
            return GCD(biggest, smallest - 1)
    else:
        return b

