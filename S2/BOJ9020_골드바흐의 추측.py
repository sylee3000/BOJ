import math
import sys
input = sys.stdin.readline

def is_prime(x):
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2, 1, -1):
        if is_prime(i) and is_prime(n-i):
            print(i, n-i)
            break