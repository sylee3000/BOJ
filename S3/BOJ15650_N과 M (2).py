N, M = map(int, input().split())
seq = []
def backtracking2(a):
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in range(a, N + 1):
            if i not in seq:
                seq.append(i)
                backtracking2(i)
                seq.pop()
backtracking2(1)