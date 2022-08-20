T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    k = 1
    res = 0
    dist = y - x
    while dist > 0:
        if dist > k:
            dist -= 2 * k
            res += 2
        else:
            dist -= k
            res += 1
        k += 1
    print(res)