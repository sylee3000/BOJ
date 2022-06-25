S, K = map(int, input().split())
result = 1
for _ in range(S % K):
    result *= (S // K) + 1
for _ in range(K - S % K):
    result *= S // K
print(result)