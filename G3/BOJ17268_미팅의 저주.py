N = int(input()) // 2

dp = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i+1):
        if j == 0:
            dp[j][i] = 1
        elif i == j:
            dp[j][i] = (dp[j-1][i-1] + dp[j-1][i]) % 987654321
        else:
            dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % 987654321
print(dp[j][i])