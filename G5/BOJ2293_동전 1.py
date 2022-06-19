n, k = map(int, input().split())
coin_value = []
dp = [0] * (k + 1)
for _ in range(n):
    coin_value.append(int(input()))
dp[0] = 1

for i in coin_value:
    for j in range(1, k+1):
        if j >= i:
            dp[j] += dp[j-i]
print(dp[k])