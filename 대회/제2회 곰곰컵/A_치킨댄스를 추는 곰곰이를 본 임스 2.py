N = int(input())
res = 0
for _ in range(N):
    D, day = input().split('-')
    if int(day) <= 90:
        res += 1
print(res)