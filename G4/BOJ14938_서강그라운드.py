from collections import deque

n, m, r = map(int, input().split())
item = deque(map(int, input().split()))
item.appendleft(0)

graph = [[16] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            
max_items = 0
for i in range(1, n+1):
    l_items = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            l_items += item[j]
    max_items = max(max_items, l_items)
print(max_items)