import sys
input = sys.stdin.readline

N, M = map(int, input().split())

title = []

for _ in range(N):
    t = list(input().split())
    title.append(t)

for _ in range(M):
    pow = int(input())
    left, right = 0, N-1
    while left < right:
        mid = (left + right) // 2
        if pow <= int(title[mid][1]):
            right = mid
        else:
            left = mid + 1
    print(title[right][0])