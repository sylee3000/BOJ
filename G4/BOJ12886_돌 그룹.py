from collections import deque

first_list = sorted(list(map(int, input().split())))
total_stone = sum(first_list)

visited_list = [[False] * (total_stone + 1) for _ in range(total_stone + 1)]
to_go_list = deque()

if total_stone % 3 == 0:
    visited_list[min(first_list)][max(first_list)] = True
    to_go_list.append([min(first_list), max(first_list)])

res = False

while to_go_list:
    i, j = to_go_list.popleft()
    k = total_stone - i - j
    if i == j == k:
        res = True
        break
    
    for a, b in (i, j), (i, k), (j, k):
        if a == b:
            continue
        elif a < b:
            new_i = 2 * a
            new_j = b - a
        else:
            new_i = 2 * b
            new_j = a - b
        new_k = total_stone - (a + b)
        new_min = min(new_i, new_j, new_k)
        new_max = max(new_i, new_j, new_k)
        
        if not visited_list[new_min][new_max]:
            visited_list[new_min][new_max] = True
            to_go_list.append([new_min, new_max])

if res:
    print(1)
else:
    print(0)