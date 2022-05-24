from collections import deque

world = []
N = int(input())
for i in range(N):
    world_l = list(map(int, input().split(' ')))
    world.append(world_l)
    
shark_row_index = -1
shark_col_index = -1
shark_size = 2
fish_num = 0
total_length = 0
for i in range(N):
    for j in range(N):
        if world[i][j] == 9:
            shark_row_index = i
            shark_col_index = j
            world[i][j] = 0
            break
            
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def fish_in_world(world):
    remain = False
    for row in world:
            for i in row:
                if i < shark_size and i > 0:
                    remain = True
                    break
    return remain

while fish_in_world(world):
    queue = deque()
    queue.append((shark_row_index, shark_col_index, 0))
    visited = [[0] * N for _ in range(N)]
    visited[shark_row_index][shark_col_index] = 0
    min_length = N ** 2
    target_idx = []

    while queue:
        x, y, pos_len = queue.popleft()
        for i in range(4):
            next_idx_x = x + dx[i]
            next_idx_y = y + dy[i]
            is_in_range = next_idx_x >= 0 and next_idx_x < N and next_idx_y >= 0 and next_idx_y < N
            if is_in_range and visited[next_idx_x][next_idx_y] == 0 and pos_len < min_length:
                    if world[next_idx_x][next_idx_y] == 0 or world[next_idx_x][next_idx_y] == shark_size:
                        queue.append((next_idx_x, next_idx_y, pos_len + 1))
                        visited[next_idx_x][next_idx_y] = 1
                    elif world[next_idx_x][next_idx_y] < shark_size:
                        if min_length == pos_len + 1:
                            if next_idx_x < target_idx[0] or (next_idx_x == target_idx[0] and next_idx_y < target_idx[1]):
                                target_idx = [next_idx_x, next_idx_y, pos_len + 1]
                        else:
                            min_length = pos_len + 1
                            target_idx = [next_idx_x, next_idx_y, pos_len + 1]
                        visited[next_idx_x][next_idx_y] = 1
    if not target_idx:
        break
    world[target_idx[0]][target_idx[1]] = 0
    shark_row_index, shark_col_index = target_idx[0], target_idx[1]
    fish_num += 1
    total_length += min_length
    if fish_num == shark_size:
        shark_size += 1
        fish_num = 0

print(total_length)