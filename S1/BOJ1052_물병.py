import math
N, K = map(int, input().split())

bin_N = []
while N > 0:
    if N % 2 == 1:
        bin_N.append(1)
    else:
        bin_N.append(0)
    N //= 2

if sum(bin_N) <= K:
    print(0)
else:
    res, count = 0, 0
    while count < K:
        a = bin_N.pop()
        if a == 1:
            count += 1
            res = 2 ** len(bin_N)
    while bin_N:
        a = bin_N.pop()
        if a == 1:
            res -= 2 ** len(bin_N)
    print(res)