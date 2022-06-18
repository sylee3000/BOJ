import math
import sys
input = sys.stdin.readline

def is_prime(x):
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n-i):
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
        break