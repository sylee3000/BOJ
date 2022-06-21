import sys
input = sys.stdin.readline

N = int(input())
min_score = []
max_score = []

for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    if i == 1:
        min_score = lst
        max_score = lst
    else:
        min_score = [min(min_score[:2]) + lst[0], min(min_score) + lst[1], min(min_score[1:]) + lst[2]]
        max_score = [max(max_score[:2]) + lst[0], max(max_score) + lst[1], max(max_score[1:]) + lst[2]]
print(max(max_score), min(min_score))