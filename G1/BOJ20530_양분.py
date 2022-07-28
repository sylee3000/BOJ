from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[a] += 1
    indegree[b] += 1

def find_cycle():
    cycle = []
    q = deque()
    
    for i in range(1, N + 1):
        if indegree[i] == 1:
            q.append(i)
            
    while q:
        k = q.popleft()
        for i in graph[k]:
            indegree[i] -= 1
            if indegree[i] == 1:
                q.append(i)
    for i in range(1, N + 1):
        if indegree[i] > 1:
            cycle.append(i)
            
    return cycle

cycle_vertex = find_cycle()
res = {}
index = 1
for i in cycle_vertex:
    res[i] = index
    index += 1
    
index = 1
for i in cycle_vertex:
    q2 = deque(graph[i])
    while q2:
        m = q2.popleft()
        if m not in res.keys():
            if graph[m]:
                for l in graph[m]:
                    if l not in res.keys():
                        q2.append(l)
            res[m] = index
    index += 1
    
for _ in range(Q):
    u, v = map(int, input().split())
    if res[u] == res[v]:
        print(1)
    else:
        print(2)