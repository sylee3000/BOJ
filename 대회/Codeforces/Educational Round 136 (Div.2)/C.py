t = int(input())

def nCm(n, m):
    r = min(n, n-m)
    u, d = 1, 1
    for i in range(n, n-r, -1):
        u *= i
    for i in range(1, r+1):
        d *= i
    return (u // d) % 998244353

for _ in range(t):
    n = int(input())
    alex, boris = 1, 0
    for i in range(4, n+1, 2):
        a, b = nCm(i-1, (i//2)-1), nCm(i-2, (i//2)-2)
        new_alex, new_boris = a + boris, b + alex
        alex, boris = new_alex, new_boris
    print(alex % 998244353, boris % 998244353, 1)