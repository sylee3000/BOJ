res = 0
k = 0
for _ in range(10):
    a, b = map(int, input().split())
    k += b-a
    res = max(res, k)
print(res)