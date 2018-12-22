import math
def CheckFermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')
def Prompt():
     a = int(input())
     b = int(input())
     c = int(input())
     n = int(input())
     check_fermat(a, b, c, n)
def IsTriangle(a, b, c):
    if a+b > c or a+c > b or b+c > a:
        print("No")
    else:
        print("Yes")
def TrianglePrompt():
    a = int(input())
    b = int(input())
    c = int(input())
    is_triangle(a, b, c)
def Recurse(n, s):
    if n == 0:
        print(s)
    else:
        Recurse(n-1, n+s)



