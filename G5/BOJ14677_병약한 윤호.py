from collections import deque

N = int(input())
med = list(input())
o = ['B', 'L', 'D']
l = 3 * N

visited = [[False] * l for _ in range(l)]
q = deque()
q.append((0, l-1, 0))
visited[0][l-1] = True

res = 0

while q:
    left, right, index = q.popleft()
    res = max(res, index)
    if index == 3 * N - 1:
        if med[left] == o[index % 3]:
            res = max(res, index+1)
    else:
        if med[left] == o[index % 3] and not visited[left+1][right]:
            q.append((left + 1, right, index + 1))
            visited[left+1][right] = True
        if med[right] == o[index % 3] and not visited[left][right-1]:
            q.append((left, right - 1, index + 1))
            visited[left][right-1] = True
print(res)