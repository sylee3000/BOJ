import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    max_s = max(s)
    second_s = 0
    max_dup, second_dup = 0, 0
    for i in s:
        if i == max_s:
            max_dup += 1
        elif i < max_s:
            if i > second_s:
                second_s = i
                second_dup = 1
            elif i == second_s:
                second_dup += 1
    if second_s == 0:
        second_s = max_s
    res = []
    for i in s:
        if i == max_s:
            if max_dup >= 2:
                res.append(0)
            else:
                res.append(i - second_s)
        else:
            res.append(i - max_s)
    print(*res)