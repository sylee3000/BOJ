N, K = map(int, input().split())
dp = [1]
for i in range(1, N + 1):
    bin_coef = []
    for j in range(i + 1):
        if j == 0 or j == i:
            bin_coef.append(1)
        else:
            bin_coef.append((dp[j-1]+dp[j]) % 10007)
    dp = bin_coef
print(dp[K] % 10007)