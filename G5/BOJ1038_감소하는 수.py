N = int(input())
cnt = -1
for a in range(10):
    for b in range(10):
        if a > b or a == 0:
            for c in range(10):
                if b > c or (a == 0 and b == 0):
                    for d in range(10):
                        if c > d or (a == 0 and b == 0 and c == 0):
                            for e in range(10):
                                if d > e or (a == 0 and b == 0 and c == 0 and d == 0):
                                    for f in range(10):
                                        if e > f or (a == 0 and b == 0 and c == 0 and d == 0 and e == 0):
                                            for g in range(10):
                                                if f > g or (a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0):
                                                    for h in range(10):
                                                        if g > h or (a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0):
                                                            for i in range(10):
                                                                if h > i or (a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0 and h == 0):
                                                                    for j in range(10):
                                                                        if i > j or (a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0 and h == 0 and i == 0):
                                                                            cnt += 1
                                                                            if cnt == N:
                                                                                res = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)
                                                                                print(int(res))
if cnt < N:
    print(-1)