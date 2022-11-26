N, D = map(int, input().split())
h = list(map(int, input().split()))
max_h = max(h)
end_h = max_h - D
res = 0
if end_h >= 0:
    for i in h:
        if i > end_h:
            res += i - end_h
else:
    res = sum(h)
print(res)