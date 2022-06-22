N, M = map(int, input().split())
seq = []
lst = sorted(list(map(int, input().split())))
def backtracking8(a):
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in range(a, N):
            k = lst[i]
            if k not in seq or i == a:
                seq.append(k)
                backtracking8(i)
                seq.pop()
backtracking8(0)