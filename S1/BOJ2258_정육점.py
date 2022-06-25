import sys
input = sys.stdin.readline

meat = []
N, M = map(int, input().split())
for _ in range(N):
    w, v = map(int, input().split())
    meat.append((w, v))
meat.sort(key=lambda x:(x[1], -x[0]))
meat_sum = 0
last_price = 0
for i in range(N):
    meat_sum += meat[i][0]
    if last_price < meat[i][1] and meat_sum >= M:
        print(meat[i][1])
        break
    last_price = meat[i][1]
if meat_sum < M:
    print(-1)