import math

N, M, K = map(int, input().split())
team = min(N // 2, M)
remain = (N - team * 2) + (M - team)
if K > remain:
    team -= math.ceil((K-remain) / 3)
print(team)