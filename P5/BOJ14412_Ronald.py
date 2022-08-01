from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
check = [False] * (N+1)
is_complete_graph = True

def bfs(i):
    global is_complete_graph
    check[i] = True
    total_len = len(graph[i])
    for j in graph[i]:
        if check[j]:
            is_complete_graph = False
        else:
            check[j] = True
            total_len += len(graph[j])
    if total_len != len(graph[i]) * (len(graph[i]) + 1):
        is_complete_graph = False

            
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, N+1):
    if not check[i]:
        bfs(i)
        if not is_complete_graph:
            break
        else:
            count += 1
        
if is_complete_graph and count <= 2:
    print("DA")
else:
    print("NE")