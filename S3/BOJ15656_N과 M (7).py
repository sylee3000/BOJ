N, M = map(int, input().split())
seq = []
lst = sorted(list(map(int, input().split())))
def backtracking7():
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in lst:
            seq.append(i)
            backtracking7()
            seq.pop()
backtracking7()