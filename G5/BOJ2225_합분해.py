N, K = map(int, input().split())
mod = int(1e9)

dp = [[1] * (N + 1) for _ in range(K + 1)]
for i in range(2, K + 1):
    sum = 0
    for j in range(N + 1):
        sum = (sum + dp[i-1][j]) % mod
        dp[i][j] = sum
print(dp[K][N])