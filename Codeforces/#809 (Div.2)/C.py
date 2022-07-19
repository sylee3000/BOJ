import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    floor = [0] * (n - 1)
    h = list(map(int, input().split()))
    
    
    if n % 2 == 1:
        res = 0
        for i in range(1, n-1, 2):
            res += max((max(h[i-1], h[i+1]) - h[i] + 1), 0)
    else:
        left = []
        right = []
        for i in range(1, n-1, 2):
            left.append(max((max(h[i-1], h[i+1]) - h[i] + 1), 0))
        for i in range(2, n-1, 2):
            right.append(max((max(h[i-1], h[i+1]) - h[i] + 1), 0))
            
        val = []
        for i in range(len(left)+1):
            val.append(sum(left[:i]) + sum(right[i:]))
        res = min(val)
    print(res)