T = int(input())
for _ in range(T):
    f = list(input().split())
    res = float(f[0])
    for i in range(1, len(f)):
        if f[i] == '@':
            res *= 3
        elif f[i] == '%':
            res += 5
        else:
            res -= 7
    print(f'{res:.2f}')