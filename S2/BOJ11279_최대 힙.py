import heapq
import sys
input = sys.stdin.readline

max_heap = []

N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -x)