N, M = map(int, input().split())
seq = []
def backtracking4(a):
    if len(seq) == M:
        print(*seq)
        return
    else:
        for i in range(a, N + 1):
            if i not in seq or i == seq[-1]:
                seq.append(i)
                backtracking4(i)
                seq.pop()
backtracking4(1)