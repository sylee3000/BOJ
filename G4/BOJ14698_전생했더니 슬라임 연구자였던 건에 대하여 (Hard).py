import heapq
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    energy = 1
    N = int(input())
    slime_list = list(map(int, input().split()))
    heapq.heapify(slime_list)
    while len(slime_list) > 1:
        s1 = heapq.heappop(slime_list)
        s2 = heapq.heappop(slime_list)
        energy *= s1 * s2
        heapq.heappush(slime_list, s1 * s2)
    print(energy % 1000000007)