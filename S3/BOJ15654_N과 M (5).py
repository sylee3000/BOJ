N, M = map(int, input().split())
seq = []
lst = sorted(list(map(int, input().split())))
def backtracking5():
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in lst:
            if i not in seq:
                seq.append(i)
                backtracking5()
                seq.pop()
backtracking5()