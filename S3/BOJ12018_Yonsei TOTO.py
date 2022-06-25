import sys
input = sys.stdin.readline
mileage = []
n, m = map(int, input().split())
for _ in range(n):
    Pi, Li = map(int, input().split())
    mile = sorted(list(map(int, input().split())), reverse=True)
    if Pi < Li:
        mileage.append(1)
    else:
        mileage.append(mile[Li-1])

limit = 0
count = 0
for i in sorted(mileage):
    limit += i
    if limit <= m:
        count += 1
    else:
        break
print(count)