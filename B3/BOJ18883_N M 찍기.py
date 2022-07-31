N, M = map(int, input().split())
k = 1
for _ in range(N):
    lst = []
    for _ in range(M):
        lst.append(k)
        k += 1
    print(*lst)