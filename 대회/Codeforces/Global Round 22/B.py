from collections import deque
import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = deque(map(int, input().split()))
    r = s.popleft()
    pre = int(math.ceil(r / (n - k + 1)))
    is_true = True
    while s and is_true:
        t = s.popleft()
        if t - r < pre:
            is_true = False
        else:
            pre = t - r
            r = t
    if is_true:
        print('Yes')
    else:
        print('No')