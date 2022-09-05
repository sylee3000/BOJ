N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (sum(c) + 1) for _ in range(N + 1)]
res = 1e4 + 1
    
for i in range(1, N + 1):
    memory, cost = m[i - 1], c[i - 1]
    for j in range(sum(c) + 1):
        dp[i][j] = dp[i-1][j]
    for j in range(cost, sum(c) + 1):
        dp[i][j] = max(dp[i][j], dp[i-1][j - cost] + memory)
        if dp[i][j] >= M:
            res = min(res, j)
print(res)