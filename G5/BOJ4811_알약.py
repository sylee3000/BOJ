while True:
    N = int(input())
    if N == 0:
        break
    
    dp = [[0] * N for _ in range(N)]
    for h in range(N):
        for w in range(h+1):
            if w == 0:
                dp[w][h] = 1
            elif w == h:
                dp[w][h] = dp[w-1][h-1] + dp[w-1][h]
            else:
                dp[w][h] = dp[w-1][h] + dp[w][h-1]
    print(dp[w][h]) 