K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))
start, end = 1, max(lan)

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in lan:
        count += i // mid
    if count < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)