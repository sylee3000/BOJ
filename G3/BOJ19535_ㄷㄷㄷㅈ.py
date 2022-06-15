import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * (N + 1)
edges = []
for _ in range(N-1):
    u, v = map(int, input().split())
    edges.append((u, v))
    cnt[u] += 1
    cnt[v] += 1
    
D_cnt = 0
G_cnt = 0

for u, v in edges:
    D_cnt += (cnt[u] - 1) * (cnt[v] - 1)

for i in cnt:
    if i >= 3:
        g_mul = 1
        g_div = 1
        for k in range(i, i - 3, -1):
            g_mul *= k
            g_div *= i - k + 1
        G_cnt += g_mul // g_div

if D_cnt > 3 * G_cnt:
    print("D")
elif D_cnt < 3 * G_cnt:
    print("G")
else:
    print("DUDUDUNGA")