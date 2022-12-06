N, M = map(int, input().split())
res = True
if (N * M) % 2 == 1:
    res = False
else:
    zero, one = 0, 0
    pattern = True
    for i in range(N):
        A = list(map(int, input().split()))
        if i == 0:
            start_pattern = A[0]
        for j in range(M):
            if A[j] == 0:
                zero += 1
            else:
                one += 1
            if (i + j) % 2 == 0:
                if A[j] != start_pattern:
                    pattern = False
            else:
                if A[j] == start_pattern:
                    pattern = False
    if zero % 2 != 0:
        res = False
if not res or pattern:
    print(-1)
else:
    print(1)