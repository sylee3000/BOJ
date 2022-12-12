N = int(input())
a = sorted(list(map(int, input().split())))

res = 0
while a:
    sum_a = sum(a)
    k1 = a.pop()
    if k1 * 2 >= sum_a:
        res += k1
        break
    else:
        k2 = a.pop()
        res += min(k1, k2)
        a.append(abs(k1 - k2))
        a.sort()
if res > 1440:
    print(-1)
else:
    print(res)