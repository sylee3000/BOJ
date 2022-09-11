from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    
    time = [0] + list(map(int, input().split()))
    res = [-1] * (N+1)
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            res[i] = time[i]
            q.append((i, res[i]))
            
    while q:
        k, t = q.popleft()
        for i in graph[k]:
            res[i] = max(res[i], t + time[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append((i, res[i]))
    print(res[int(input())])