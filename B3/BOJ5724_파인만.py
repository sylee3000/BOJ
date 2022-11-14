while True:
    N = int(input())
    if N == 0:
        break
    res = 0
    for i in range(1, N+1):
        res += i * i
    print(res)