from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001
pos = deque([N])
min_time = 0

while True:
    next_pos = deque()
    while pos:
        p = pos.popleft()
        index = p
        if index == 0 and K != 0:
            next_pos.append(1)
        else:
            while index <= 100000 and visited[index] == False:
                visited[index] = True
                if visited[index-1] == False:
                    next_pos.append(index-1)
                if index < 100000 and visited[index+1] == False:
                    next_pos.append(index+1)
                index *= 2
    if visited[K] == True:
        print(min_time)
        break
    pos = next_pos
    min_time += 1
