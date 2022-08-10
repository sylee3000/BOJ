N = int(input())
lst = list(map(int, input().split()))

res = 0
score = 0
for i in range(N):
    if lst[i] == 1:
        score += 1
        res += score
    else:
        score = 0
print(res)