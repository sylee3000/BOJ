N = int(input())

k = N
res = 0

while True:
    res += 1
    a, b = k // 10, k % 10
    c, d = (a + b) % 10, b * 10
    k = c + d
    
    if N == k:
        break
print(res)