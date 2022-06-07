from collections import deque

com = int(input())
connect = [[0] * com for i in range(com)]

line_num = int(input())
for _ in range(line_num):
    x, y = map(int, input().split())
    connect[x-1][y-1] = 1
    connect[y-1][x-1] = 1
infected = [0] * com
deque = deque([0])
infected[0] = 1
while deque:
    index = deque.popleft()
    for i in range(com):
        if infected[i] == 0 and connect[index][i] == 1:
            infected[i] = 1
            deque.append(i)
print(sum(infected) - 1)