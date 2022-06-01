from collections import deque

M, N = map(int, input().split())
tomato_list = [[x for x in list(map(int, input().split()))] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    else:
        return False

def tomato():
    lst = deque()
    for i in range(N):
        for j in range(M):
            if tomato_list[i][j] == 1:
                visited[i][j] = True
                lst.append([i, j, 0])
    time = 0
    while lst:
        idx_n, idx_m, t = map(int, lst.popleft())
        if t > time:
            time = t
        
        for i in range(4):
            x = idx_n + dx[i]
            y = idx_m + dy[i]
            if in_range(x, y):
                if tomato_list[x][y] == 0 and visited[x][y] == False:
                    tomato_list[x][y] = 1
                    visited[x][y] = True
                    lst.append([x, y, t + 1])
    return time

time = tomato()
       
for i in range(N):
    for j in range(M):
        if tomato_list[i][j] == 0:
            time = -1

print(time)