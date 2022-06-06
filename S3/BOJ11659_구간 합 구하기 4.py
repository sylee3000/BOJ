import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [x for x in map(int, input().split())]
sum_of_num = []
for i in range(len(num)):
    if not sum_of_num:
        sum_of_num.append(num[i])
    else:
        sum_of_num.append(num[i] + sum_of_num[i-1])
for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(sum_of_num[end-1])
    else:
        print(sum_of_num[end-1]-sum_of_num[start-2])