import math

N, K, M = map(int, input().split())
N_lst = []
K_lst = []

while N > 0:
    N_lst.append(N % M)
    N -= (N % M)
    N = N // M
    
while K > 0:
    K_lst.append(K % M)
    K -= (K % M)
    K = K // M

min_len = min(len(N_lst), len(K_lst))

res = 1

for i in range(min_len):
    n, k = N_lst[i], K_lst[i]
    if n < k:
        res = 0
    else:
        res = (res * math.comb(n, k)) % M
        
print(res)