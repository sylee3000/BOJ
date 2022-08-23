N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph_line = list(input())
    graph.append(graph_line)

h, v = 0, 0

for i in range(N):
    check = True
    for j in range(M):
        if graph[i][j] != '.':
            check = False
    if check:
        h += 1
        
for i in range(M):
    check = True
    for j in range(N):
        if graph[j][i] != '.':
            check = False
    if check:
        v += 1
        
print(max(h, v))