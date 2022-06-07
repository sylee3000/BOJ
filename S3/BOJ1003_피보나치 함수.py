T = int(input())
fib_0 = [1,0,1]
fib_1 = [0,1,1]
for i in range(T):
    N = int(input())
    if N >= len(fib_0):
        for i in range(len(fib_0), N + 1):
            fib_0.append(fib_0[-2] + fib_0[-1])
            fib_1.append(fib_1[-2] + fib_1[-1])
    print(fib_0[N], fib_1[N])