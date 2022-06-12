import heapq
import sys
input = sys.stdin.readline

abs_heap = []

N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if not abs_heap:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
    else:
        heapq.heappush(abs_heap, (abs(x), x))