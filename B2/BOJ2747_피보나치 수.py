n = int(input())
dp = [0, 1]
i = 2
while i <= n:
    dp.append(dp[i-2]+dp[i-1])
    i += 1
print(dp[n])