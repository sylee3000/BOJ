N = int(input())
dp = [1] * (N+1)

k = 2
while k <= N:
    for i in range(k, N+1):
        dp[i] = (dp[i] + dp[i-k]) % int(1e9) 
    k *= 2
print(dp[N])