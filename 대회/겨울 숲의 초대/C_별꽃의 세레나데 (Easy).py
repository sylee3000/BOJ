N = int(input())
res = 1
for i in range(N, 1, -1):
    res += N / (i - 1)
print(res)