import math

M, N = map(int, input().split())
list = []
def is_prime(i):
    if i == 1:
        return False
    for a in range(2, int(math.sqrt(i)) + 1):
        if i % a == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)