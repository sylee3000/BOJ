N = int(input())
score = 0
for _ in range(N):
    a, d, g = map(int, input().split())
    if a == d + g:
        score = max(score, a * (d + g) * 2)
    else:
        score = max(score, a * (d + g))
print(score)