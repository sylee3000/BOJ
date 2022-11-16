N = int(input())
for _ in range(N):
    M = int(input())
    tk, td, ta = [], [], []
    for _ in range(M):
        K, D, A = map(int, input().split())
        tk.append(K)
        td.append(D)
        ta.append(A)
    gk, gd, ga = map(int, input().split())
    res = 0
    for i in range(M):
        donation = gk * tk[i] - gd * td[i] + ga * ta[i]
        if donation > 0:
            res += donation
    print(res)