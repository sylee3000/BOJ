grid = []
for _ in range(9):
    l = list(map(int, input().split()))
    grid.append(l)

max_num = 0
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if max_num < grid[i][j]:
            max_num = grid[i][j]
            a, b = i, j
print(max_num)
print(a+1, b+1)