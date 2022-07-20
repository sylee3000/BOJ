import heapq
import sys
input = sys.stdin.readline

heap_left = []
heap_right = []

N, M = map(int, input().split())
book = list(map(int, input().split()))
while book:
    b = book.pop()
    if b > 0:
        heapq.heappush(heap_right, -b)
    else:
        heapq.heappush(heap_left, b)
        
point = []
index = 0
while heap_left:
    h_l = heapq.heappop(heap_left)
    if index % M == 0:
        heapq.heappush(point, h_l)
    index += 1
    
index = 0
while heap_right:
    h_r = heapq.heappop(heap_right)
    if index % M == 0:
        heapq.heappush(point, h_r)
    index += 1

last = heapq.heappop(point)
print(-(last + sum(point) * 2))