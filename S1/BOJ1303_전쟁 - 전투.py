from collections import deque

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    color = graph[i][j]
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 0
    while q:
        a, b = q.popleft()
        count += 1
        for k in range(4):
            next_a, next_b = a + dx[k], b + dy[k]
            if 0 <= next_a < N and 0 <= next_b < M and graph[next_a][next_b] == color and not visited[next_a][next_b]:
                q.append((next_a, next_b))
                visited[next_a][next_b] = True
    return count ** 2

res = {'B': 0, 'W': 0}

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            res[graph[i][j]] += bfs(i, j)
print(res['W'], res['B'])