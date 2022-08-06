import math

N = int(input())

p = math.log2(N)

if p == int(p):
    print(1)
else:
    print(0)