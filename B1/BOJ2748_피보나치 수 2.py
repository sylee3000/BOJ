n = int(input())
fib_data = {0:0, 1:1}
def fibonacci(n):
    if n == 0 or n == 1:
        return fib_data[n]
    else:
        for i in range(2, n + 1):
            fib_data[i] = fib_data[i - 1] + fib_data[i - 2]
        return fib_data[n]
print(fibonacci(n))