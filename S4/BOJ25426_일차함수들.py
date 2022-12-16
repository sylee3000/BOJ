N = int(input())
a_s = []
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    res += b
    a_s.append(a)
a_s.sort(reverse=True)
for i in a_s:
    res += i * N
    N -= 1
print(res)