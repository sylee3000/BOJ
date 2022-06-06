import sys
input = sys.stdin.readline

N = int(input())
number_list = sorted([x for x in map(int, input().split())])
M = int(input())
find_list = [x for x in map(int, input().split())]

for i in find_list:
    start, end = 0, N-1
    is_in_list = 0
    while start <= end:
        mid = (start + end) // 2
        if i == number_list[mid]:
            is_in_list = 1
            break
        elif i < number_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    print(is_in_list, end=' ')