from mymath import *

poly = polynomial([1, 1, -1])
guess = 1
tolerance = 1 * 10**-2

wortel = poly.rootNewton(guess, tolerance)
print(wortel)







