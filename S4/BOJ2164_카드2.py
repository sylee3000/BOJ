from collections import deque

N = int(input())
q = deque([x for x in range(1, N + 1)])
while len(q) > 1:
    q.popleft()
    to_bottom = q.popleft()
    q.append(to_bottom)
print(q.pop())