import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
chon = [[False] * n for _ in range(n)]
visited = [False] * n
for _ in range(m):
    p, s = map(int, input().split())
    chon[p-1][s-1] = True
    chon[s-1][p-1] = True
find = deque()
find.append((a-1, 0))
result = 0
while find:
    k, chons = find.popleft()
    visited[k] = True
    if k == b-1:
        result = chons
        break
    for i in range(n):
        if chon[k][i] == True and visited[i] == False:
            find.append((i, chons + 1))
else:
    result = -1
print(result)