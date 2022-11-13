import math

A, B = map(int, input().split())
k = B // A
m = int(math.sqrt(k))
res1, res2 = 1e8+1, 1e8+1

def gcd(x, y):
    if x == 0 or y == 0:
        return max(x, y)
    else:
        return gcd(max(x,y) % min(x,y), min(x,y))

while m > 0:
    if k / m == k // m:
        n1, n2 = m, k // m
        if gcd(n1, n2) == 1:
            if res1 + res2 > n1 + n2:
                res1, res2 = n1, n2
    m -= 1

print(A * min(res1, res2), A * max(res1, res2))