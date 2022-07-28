from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

vertical = [[False] * (M-1) for _ in range(N)]
horizontal = [[False] * M for _ in range(N-1)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
area_size = []

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    area = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if i % 2 == 0 and 0 <= x - (i // 2) < N-1:
                    if not visited[next_x][next_y] and not horizontal[x - (i // 2)][y]:
                        queue.append([next_x, next_y])
                        visited[next_x][next_y] = True
                        area += 1
                elif i % 2 == 1 and 0 <= y - (i // 2) < M-1:
                    if not visited[next_x][next_y] and not vertical[x][y - (i // 2)]:
                        queue.append([next_x, next_y])
                        visited[next_x][next_y] = True
                        area += 1
    area_size.append(area)
                    

T = int(input())
for _ in range(T):
    Sx, Sy, Ex, Ey = map(int, input().split())
    if Sx == Ex and Sx != 0 and Sx != N:
        for i in range(min(Sy, Ey), max(Sy, Ey)):
            horizontal[Sx-1][i] = True
    elif Sy == Ey and Sy != 0 and Sy != M:
        for i in range(min(Sx, Ex), max(Sx, Ex)):
            vertical[i][Sy-1] = True
            
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j)
print(max(area_size))
print(min(area_size))