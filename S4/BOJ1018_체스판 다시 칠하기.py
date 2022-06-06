w_f = ['W','B','W','B','W','B','W','B']
b_f = ['B','W','B','W','B','W','B','W']
mk1 = [w_f, b_f, w_f, b_f, w_f, b_f, w_f, b_f]

N, M = map(int, input().split())
base = []
for _ in range(N):
    base.append(input())

min_repaint = N * M
for i in range(N - 7):
    for j in range(M - 7):
        mk1_repaint = 0
        for a in range(8):
            for b in range(8):
                if base[i+a][j+b] != mk1[a][b]:
                    mk1_repaint += 1
        min_repaint = min(min_repaint, mk1_repaint, 64 - mk1_repaint)
print(min_repaint)