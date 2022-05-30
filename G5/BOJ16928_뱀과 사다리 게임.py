N, M = map(int, input().split())
ladder_and_snake = {}
visited = [0] * 100
for i in range(N + M):
    k, v = map(int, input().split())
    ladder_and_snake[k] = v
count = 0
pos = {0:[1]}
while True:
    available_pos = []
    for x in pos[count]:
        for i in range(1, 7):
            if (x + i <= 100 and visited[x + i - 1]) or x + i > 100:
                continue
            visited[x + i - 1] = 1
            if x + i in ladder_and_snake.keys():
                available_pos.append(ladder_and_snake[x + i])
                visited[ladder_and_snake[x + i] - 1] = 1
            else:
                available_pos.append(x + i)
    count += 1
    if available_pos.count(100) > 0:
        break
    else:
        pos[count] = available_pos
print(count)