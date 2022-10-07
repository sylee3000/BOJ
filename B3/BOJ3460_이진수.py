T = int(input())
for _ in range(T):
    n = int(input())
    k = 0
    res = []
    while n > 0:
        if n % 2 == 1:
            res.append(k)
            n = (n - 1) // 2
        else:
            n = n // 2
        k += 1
    print(*res)