N = int(input())
K = int(input())
start, end = 1, N**2
mid = 0
while start <= end:
    mid = (start+end) // 2
    seq = 0
    for i in range(1, N+1):
        seq += min(mid // i, N)
    if seq >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)