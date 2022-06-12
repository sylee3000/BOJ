import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

for i in range(len(count)):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)