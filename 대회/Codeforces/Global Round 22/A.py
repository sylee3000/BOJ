from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = deque(map(int, input().split()))
    b = deque(map(int, input().split()))
    fire, frost = deque(), deque()
    for _ in range(n):
        x, y = a.popleft(), b.popleft()
        if x == 0:
            fire.append(y)
        else:
            frost.append(y)
    fire_sorted, frost_sorted = deque(sorted(fire)), deque(sorted(frost))
    fire_len, frost_len = len(fire), len(frost)
    res = 0
    if fire_len > frost_len:
        for _ in range(fire_len - frost_len):
            res += fire_sorted.popleft()
    elif fire_len < frost_len:
        for _ in range(frost_len - fire_len):
            res += frost_sorted.popleft()
    else:
        fire_min, frost_min = fire_sorted.popleft(), frost_sorted.popleft()
        res += min(fire_min, frost_min) + max(fire_min, frost_min) * 2
    res += (sum(fire_sorted) + sum(frost_sorted)) * 2
    print(res)