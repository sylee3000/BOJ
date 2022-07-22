from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
path = [[] for _ in range(N + 1)]
for i in range(1, N):
    i_n = int(input())
    path[i] = list(map(int, input().split()))
visited = [False] * (N + 1)
q = deque()
q.append(1)
visited[1] = True
have_cycle = False
while q and not have_cycle:
    t = q.popleft()
    visited[t] = True
    for j in path[t]:
        if visited[j]:
            for k in path[j]:
                if visited[k]:
                    have_cycle = True
                    break
        else:
            q.append(j)
if have_cycle:
    print('CYCLE')
else:
    print('NO CYCLE')