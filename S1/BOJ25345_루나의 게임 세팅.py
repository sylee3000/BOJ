import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
A = list(map(int, input().split()))
def bin_coef(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res = res * i 
    for i in range(1, k+1):
        res = res // i
    res = res % 1000000007
    return res
def pow_2(k):
    if k == 0:
        return 1
    return 2 * pow_2(k-1) % 1000000007
print(bin_coef(N, K) * pow_2(K - 1) % 1000000007)