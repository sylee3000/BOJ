import sys
input = sys.stdin.readline

T = int(input())

k = [[] for _ in range(10)]
for i in range(10):
    c = i
    while True:
        if c == 0:
            k[i].append(10)
        else:
            k[i].append(c)
        c = (c * i) % 10
        if c == i:
            break

for _ in range(T):
    a, b = map(int, input().split())
    print(k[a % 10][(b - 1) % len(k[a % 10])])