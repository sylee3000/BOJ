R, C = map(int, input().split())
maze = []
fire = []
jihun = []
for i in range(R):
    maze_l = list(input())
    for j in range(C):
        if maze_l[j] == 'J':
            jihun.append((i, j))
        elif maze_l[j] == 'F':
            fire.append((i, j))
    maze.append(maze_l)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

res = -1
cnt = 0


while res < 0 and jihun:
    cnt += 1
    new_fire = []
    for i, j in fire:
        for k in range(4):
            new_i, new_j = i + dx[k], j + dy[k]
            if 0 <= new_i < R and 0 <= new_j < C:
                if maze[new_i][new_j] == '.' or maze[new_i][new_j] == 'J':
                    new_fire.append((new_i, new_j))
                    maze[new_i][new_j] = 'F'
    new_jihun = []
    for i, j in jihun:
         for k in range(4):
             new_i, new_j = i + dx[k], j + dy[k]
             if new_i < 0 or new_i >= R or new_j < 0 or new_j >= C:
                 res = cnt
             elif maze[new_i][new_j] == '.':
                 new_jihun.append((new_i, new_j))
                 maze[new_i][new_j] = 'J'
    fire = new_fire
    jihun = new_jihun
if res < 0:
    print('IMPOSSIBLE')
else:
    print(res)