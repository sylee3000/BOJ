fib = [1, 1]

n = int(input())
if n >= 2:
    for i in range(2, n + 1):
        fib.append((fib[i-2]+fib[i-1]+1) % int(1e9+7))
print(fib[n])