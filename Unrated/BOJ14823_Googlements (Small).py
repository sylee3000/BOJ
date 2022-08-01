from collections import deque
from itertools import permutations
seq = []
seq_index = []
used_q = []

def backtracking(q, permutation_lst, l):
    global used_q
    while permutation_lst:
        i = permutation_lst.pop()
        next = ""
        for j in i:
            next += str(j)
        if next not in used_q and next not in q:
            if sum(i) <= l:
                q.append(next)
            else:
                used_q.append(next)
    
T = int(input())
for i in range(1, T+1):
    G = input()
    l = len(G)
    q = deque()
    q.append(G)
    used_q = []
    while q:
        k = q.popleft()
        used_q.append(k)
        part_sum = 0
        lst = []
        seq = []
        seq_index = []
        for j in range(l):
            part_sum += int(k[j])
            for _ in range(int(k[j])):
                lst.append(j+1)
        if part_sum <= l:
            for _ in range(l-part_sum):
                lst.append(0)
            permutation_lst = set(permutations(lst, l))
            backtracking(q, permutation_lst, l)
    print(f'Case #{i}: {len(used_q)}')