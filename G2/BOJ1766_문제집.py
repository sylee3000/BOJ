import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1 

q = []
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
    
res = []    
while q:
    x = heapq.heappop(q)
    res.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)
print(*res)