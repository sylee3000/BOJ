import sys

input = sys.stdin.readline
N = int(input())
list = []
for _ in range(N):
    i = int(input())
    list.append(i)
list.sort()
for l in list:
    print(l)