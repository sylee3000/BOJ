def g(N):
    res = 0
    for i in range(1, N+1):
        res += (N // i) * i
    return res

N = int(input())
print(g(N))