import heapq
import sys
input = sys.stdin.readline

min_heap = []

N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, x)