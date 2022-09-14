import heapq

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A_heap = []
    B_heap = []
    for i in A:
        heapq.heappush(A_heap, -i)
    
    for i in B:
        heapq.heappush(B_heap, -i)
    
    res = 0
    nA, nB = -heapq.heappop(A_heap), -heapq.heappop(B_heap)
    while True:
        if nA > nB:
            res += len(B_heap) + 1
            if A_heap:
                nA = -heapq.heappop(A_heap)
            else:
                break
        elif B_heap:
            nB = -heapq.heappop(B_heap)
        else:
            break
    print(res)