N = int(input())
area = [[0] * 500 for _ in range(500)]
res = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if area[i][j] != 1:
                area[i][j] = 1
                res += 1
print(res)