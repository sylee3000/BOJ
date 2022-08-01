from collections import deque
used_q = []

def backtracking(q, dict, l, part, part_sum):
    global used_q
    if len(part) == l:
        if part not in used_q and part not in q:
            if part_sum <= l:
                q.append(part)
            else:
                used_q.append(part)
            return
    else:
        for i in dict.keys():
            if dict[i] > 0 :
                new_part = part + str(i)
                part_sum += i
                dict[i] -= 1
                backtracking(q, dict, l, new_part, part_sum)
                part_sum -= i
                dict[i] += 1

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
        dict = {}
        seq = []
        for j in range(l):
            part_sum += int(k[j])
            dict[j+1] = int(k[j])
        if part_sum <= l:
            dict[0] = l-part_sum
            backtracking(q, dict, l, '', 0)
    print(f'Case #{i}: {len(used_q)}')