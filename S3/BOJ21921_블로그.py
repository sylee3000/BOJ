from collections import deque

N, X = map(int, input().split())
visit = deque(map(int, input().split()))
part_deque = deque()
part_sum = 0
max_sum = 0
cnt = 0

for i in range(N + X):
    a = visit.popleft()
    if len(part_deque) < X:
        part_deque.append(a)
        visit.append(a)
        part_sum += a
        if len(part_deque) == X:
            if part_sum > max_sum:
                max_sum = part_sum
                cnt = 1
    else:
        part_deque.append(a)
        if i < N:
            part_sum += a
        part_sum -= part_deque.popleft()
        if part_sum > max_sum:
            max_sum = part_sum
            cnt = 1
        elif part_sum == max_sum and cnt != 0:
            cnt += 1
if cnt == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)