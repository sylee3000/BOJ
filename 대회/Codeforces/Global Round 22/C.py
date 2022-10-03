from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = deque(map(int, input().split()))
    odd, even = 0, 0
    while a:
        k = a.popleft()
        if k % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd % 4 == 1:
        if even % 2 == 1:
            print('Alice')
        else:
            print('Bob')
    elif odd % 4 == 2:
        print('Bob')
    else:
        print('Alice')