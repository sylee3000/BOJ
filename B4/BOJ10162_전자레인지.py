T = int(input())
time = [300, 60, 10]
if T % 10 != 0:
    print(-1)
else:
    for t in time:
        print(T//t, end=' ')
        T = T % t