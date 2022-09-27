while True:
    N = list(map(int, input().split()))
    if N[0] == 0:
        break
    else:
        S = []
        re = 0
        for i in N[1:]:
            if i != re:
                S.append(i)
            re = i
        print(*S, "$")