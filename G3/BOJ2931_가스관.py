R, C = map(int, input().split())
Europe = []
connection = [['-', '1', '2', '+'], ['-', '3', '4', '+'], ['|', '1', '4', '+'], ['|', '2', '3', '+']]

for i in range(R):
    EU_line = list(input())
    for j in range(C):
        if EU_line[j] == 'M':
            Mx, My = i, j
    Europe.append(EU_line)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(4):
    if 0 <= Mx + dx[i] < R and 0 <= My + dy[i] < C:
        if Europe[Mx + dx[i]][My + dy[i]] != '.' and Europe[Mx + dx[i]][My + dy[i]] != 'Z':
            dir = i
res_shape = '.'

while True:
    Mx = Mx + dx[dir]
    My = My + dy[dir]

    if Europe[Mx][My] == '1':
        if dir == 0:
            dir = 3
        elif dir == 2:
            dir = 1
    elif Europe[Mx][My] == '2':
        if dir == 0:
            dir = 2
        elif dir == 3:
            dir = 1
    elif Europe[Mx][My] == '3':
        if dir == 1:
            dir = 2
        elif dir == 3:
            dir = 0
    elif Europe[Mx][My] == '4':
        if dir == 1:
            dir = 3
        elif dir == 2:
            dir = 0
    elif Europe[Mx][My] == '.':
        res_x, res_y = Mx, My
        if res_shape == '|' or res_shape == '-':
            res_shape = '+'
            
        elif dir == 0 or dir == 1:
            if 0 <= Mx + dx[dir] < R and 0 <= My + dy[dir] < C:
                if Europe[Mx + dx[dir]][My + dy[dir]] in connection[dir]:
                    res_shape = '-'
            if res_shape == '.':
                if 0 <= Mx + dx[2] < R and 0 <= My + dy[2] < C:
                    if Europe[Mx + dx[2]][My + dy[2]] in connection[2]:
                        if dir == 0:
                            res_shape = '2'
                        else:
                            res_shape = '3'
                        dir = 2
                else:
                    if dir == 0:
                        res_shape = '1'
                    else:
                        res_shape = '4'
                    dir = 3
        else:
            if 0 <= Mx + dx[dir] < R and 0 <= My + dy[dir] < C: 
                if Europe[Mx + dx[dir]][My + dy[dir]] in connection[dir]:
                    res_shape = '|'
            if res_shape == '.':
                if 0 <= Mx + dx[0] < R and 0 <= My + dy[0] < C:
                    if Europe[Mx + dx[0]][My + dy[0]] in connection[0]:
                        if dir == 2:
                            res_shape = '4'
                        else:
                            res_shape = '3'
                        dir = 0
                else:
                    if dir == 2:
                        res_shape = '1'
                    else:
                        res_shape = '2'
                    dir = 1
    elif Europe[Mx][My] == 'Z':
        break
print(res_x + 1, res_y + 1, res_shape)