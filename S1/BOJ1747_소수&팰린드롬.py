import math

N = int(input())
def is_prime(i):
    if i == 1:
        return False
    for a in range(2, int(math.sqrt(i)) + 1):
        if i % a == 0:
            return False
    return True

while True:
    if is_prime(N):
        if str(N) == str(N)[::-1]:
            print(N)
            break
    N = N + 1