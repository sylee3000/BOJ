T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        c = coin[i - 1]
        for j in range(c, target + 1):
            dp[j] = dp[j] + dp[j - c]
    print(dp[target])