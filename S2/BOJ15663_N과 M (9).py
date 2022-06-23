N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
seq = []
seq_index = []
seq_print = []
def backtracking9(a):
    if len(seq) == M:
        seq_print.append(tuple(seq))
        return
    else:
        for i in range(a, N):
            if i not in seq_index:
                seq.append(lst[i])
                seq_index.append(i)
                backtracking9(i + 1)
                seq.pop()
                seq_index.pop()
backtracking9(0)
seq_print = sorted(set(seq_print))
for i in seq_print:
    print(*i)