N, K = map(int, input().split())
result = 1
for i in range(1, K + 1):
    result *= N - i + 1
    result = result // i
print(result)