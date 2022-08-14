V, E = map(int, input().split())
graph = [[] * (V + 1)]
indegree = [0] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
print(indegree)