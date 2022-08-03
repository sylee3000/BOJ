from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
res = 0
part_deque = deque()
part_sum = 0

for i in range(N + K):
    a = A.popleft()
    if len(part_deque) < K:
        part_deque.append(a)
        A.append(a)
        part_sum += a
    else:
        part_deque.append(a)
        part_sum += a
        part_sum -= part_deque.popleft()
        if part_sum > res:
            res = part_sum
print(res)