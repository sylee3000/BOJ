import sys, heapq
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra(cave, cost, x, y):
    k = len(cave)
    queue = []
    
    heapq.heappush(queue, (cave[x][y], x, y))
    while queue:
        l_cost, l_x, l_y = heapq.heappop(queue)
        if l_cost > cost[l_x][l_y]:
            continue
        
        for i in range(4):
            side_x, side_y = l_x + dx[i], l_y + dy[i]
            if 0 <= side_x < k and 0 <= side_y < k:
                next_pos_cost = cave[side_x][side_y]
                next_cost = l_cost + next_pos_cost
                if next_cost < cost[side_x][side_y]:
                    heapq.heappush(queue, (next_cost, side_x, side_y))
                    cost[side_x][side_y] = next_cost
                    
    return cost[k-1][k-1]

testcase_number = 1

while True:
    N = int(input())
    if N == 0:
        break
    cave = []
    for _ in range(N):
        line = list(map(int, input().split()))
        cave.append(line)
    cost = [[int(2e5)] * N for _ in range(N)]
    answer = dijkstra(cave, cost, 0, 0)
    
    print(f'Problem {testcase_number}: {answer}')
    testcase_number += 1