from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
visited[1] = 1
for i in graph[1]:
    q.append(i)
    visited[i] = 1
    
while q:
    k = q.popleft()
    for i in graph[k]:
        if visited[i] == 0:
            visited[i] = 1

print(sum(visited)-1)