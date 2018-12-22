import time

t1 = time.perf_counter()

n = 10
prime = [True] * n

for p in range (2, n):
    if p ** 2 > n:
        break
    if prime[p] == True:
        for i in range(p**2,n, p):
                prime[i] = False

x = [p for i in range(2,n) if prime[i] == True]

print(len(x))
t2 = time.perf_counter()
print('', t2-t1)



