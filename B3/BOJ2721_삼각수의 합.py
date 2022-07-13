T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    tmp = 1
    for i in range(1, n+1):
        tmp += i+1
        ans += i * tmp
    print(ans)