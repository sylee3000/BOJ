from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    a = []
    pre = d.popleft()
    a.append(pre)
    op = True
    for i in range(n-1):
        if op:
            k = d.popleft()
            if pre < k or k == 0:
                k += pre
                a.append(k)
                pre = k
            else:
                op = False
    if op:
        print(*a)
    else:
        print(-1)