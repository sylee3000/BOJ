import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
LP = list(map(int, input().split()))
streamer = []
for _ in range(N-1):
    streamer.append(list(map(int, input().split())))

res = 0
for i in range(N-1):
    diff = 0
    for j in range(M):
        diff += abs(streamer[i][j] - LP[j])
    if diff > 2000:
        res += 1
if res >= math.ceil((N-1) / 2):
    print('YES')
else:
    print('NO')