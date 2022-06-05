N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))


for i in B:
    start, end = 0, N-1
    while True:
        if start > end:
            print(0)
            break
        mid = (start + end) // 2
        if A[mid] == i:
            print(1)
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1  