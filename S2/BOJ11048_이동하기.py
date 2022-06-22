import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = maze[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + maze[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + maze[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + maze[i][j]
            
print(dp[N-1][M-1])