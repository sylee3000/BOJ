N = int(input())
graph = [[] * (N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
