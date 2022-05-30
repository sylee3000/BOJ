from collections import deque

N, K = map(int, input().split())
q = deque([x for x in range(1, N + 1)])
print("<", end='')
cnt = 0
while q:
    cnt = (cnt + 1) % K
    if cnt == 0:
        if len(q) == 1:
            print(str(q.popleft()), end='')
        else:
            print(str(q.popleft()) + ", ", end='')
    else:
        q.append(q.popleft())
print(">")