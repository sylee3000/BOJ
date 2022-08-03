import math

while True:
    n, k = map(int, input().split())
    if n == k and n == 0:
        break
    print(math.comb(n, k))