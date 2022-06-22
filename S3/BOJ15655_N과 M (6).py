N, M = map(int, input().split())
seq = []
lst = sorted(list(map(int, input().split())))
def backtracking6(a):
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in range(a, N):
            k = lst[i]
            if k not in seq:
                seq.append(k)
                backtracking6(i)
                seq.pop()
backtracking6(0)