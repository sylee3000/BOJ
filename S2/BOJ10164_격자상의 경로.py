N, M, K = map(int, input().split())

if K != 0:
    A, B = (K - 1) // M, (K - 1) % M
    r1 = [[0] * (B+1) for _ in range(A+1)]
    r2 = [[0] * (M-B) for _ in range(N-A)]
    
    for i in range(B+1):
        r1[0][i] = 1
    for i in range(A+1):
        r1[i][0] = 1
    for i in range(1, A+1):
        for j in range(1, B+1):
            r1[i][j] = r1[i-1][j] + r1[i][j-1]
    
    for i in range(M-B):
        r2[0][i] = 1
    for i in range(N-A):
        r2[i][0] = 1
    for i in range(1, N-A):
        for j in range(1, M-B):
            r2[i][j] = r2[i-1][j] + r2[i][j-1]
    
    print(r1[A][B] * r2[N-A-1][M-B-1])
else:
    r = [[0] * M for _ in range(N)]
    for i in range(M):
        r[0][i] = 1
    for i in range(N):
        r[i][0] = 1
    for i in range(1, N):
        for j in range(1, M):
            r[i][j] = r[i-1][j] + r[i][j-1]
    print(r[N-1][M-1])