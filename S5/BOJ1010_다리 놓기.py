T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    res = 1
    for i in range(M, M - N, -1):
        res *= i
    for i in range(1, N + 1):
        res = res // i
    print(res)