pos_x = []
pos_y = []
for _ in range(3):
    x, y = map(int, input().split())
    if x not in pos_x:
        pos_x.append(x)
    else:
        pos_x.remove(x)
    if y not in pos_y:
        pos_y.append(y)
    else:
        pos_y.remove(y)
print(pos_x[0], pos_y[0])