T = int(input())
for _ in range(T):
    n, a, b, c = map(int, input().split())
    if a + b + c >= 55 and a / 35 >= 0.3 and b / 25 >= 0.3 and c / 40 >= 0.3:
        pf = 'PASS'
    else:
        pf = 'FAIL'
    print(n, a + b + c, pf)