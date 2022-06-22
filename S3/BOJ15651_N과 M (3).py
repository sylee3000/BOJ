N, M = map(int, input().split())
seq = []
def backtracking3():
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in range(1, N + 1):
            seq.append(i)
            backtracking3()
            seq.pop()
backtracking3()