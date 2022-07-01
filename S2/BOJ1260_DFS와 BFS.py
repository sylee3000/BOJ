from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

    
def DFS(V):
    print(V+1, end=' ')
    visited[V] = 1
    for i in range(N):
        if graph[V][i] == 1 and visited[i] == 0:
            DFS(i)
            
def BFS(V):
    visited[V] = 1
    bfs_list = deque([V])
    while bfs_list:
        index = bfs_list.popleft()
        print(index + 1, end=' ')
        for i in range(N):
            if graph[index][i] == 1 and visited[i] == 0:
                bfs_list.append(i)
                visited[i] = 1

DFS(V-1)
print()
visited = [0] * N
BFS(V-1)