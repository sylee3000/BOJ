N = int(input())
A = list(map(int, input().split()))

max = -100000000
min = 100000000

for i in range(N):
    if A[i] < min:
        min = A[i]
    if A[i] > max:
        max = A[i]
        
print(min, max)