import heapq, sys
input = sys.stdin.readline

heap_left = []
heap_right = []

N = int(input())
for _ in range(N):
    k = int(input())
    if len(heap_left) == 0:
        heapq.heappush(heap_left, -k)
        left_marker = -k
        right_marker = 1e5
    elif len(heap_left) == len(heap_right):
        if k > right_marker:
            new_marker = heapq.heappop(heap_right)
            heapq.heappush(heap_left, -new_marker)
            heapq.heappush(heap_right, k)
            left_marker = -new_marker
            right_marker = heap_right[0]
        else:
            heapq.heappush(heap_left, -k)
            left_marker = heap_left[0]
    else:
        if k < (-left_marker):
            new_marker = -heapq.heappop(heap_left)
            heapq.heappush(heap_right, new_marker)
            heapq.heappush(heap_left, -k)
            right_marker = new_marker
            left_marker = heap_left[0]
        else:
            heapq.heappush(heap_right, k)
            right_marker = heap_right[0]
    print(-left_marker)