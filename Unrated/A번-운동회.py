import math

N, M, a, K = map(int, input().split())
if N-1 <= a-K:
    max_rank = N
else:
    max_rank = a-K+1

min_rank = math.ceil((a-K) / (M)) + 1

print(max_rank, min_rank)