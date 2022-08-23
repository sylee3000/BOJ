K = int(input())
fib = [1, 1]
if K >= 2:
    for i in range(2, K):
        fib.append(fib[i-2] + fib[i-1])
print(fib[K-1])