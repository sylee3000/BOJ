fib_data = {}
def f_s(x):
    if x == 0:
        fib_data[0] = 0
        return 0
    elif x == 1 or x == 2:
        fib_data[x] = 1
        return 1
    else:
        if x in fib_data.keys():
            return fib_data[x]
        elif x % 2 == 0:
            fib_data[x] = (f_s(x // 2) * (f_s(x // 2 + 1) + f_s(x // 2 - 1))) % 1000000007
            return (f_s(x // 2) * (f_s(x // 2 + 1) + f_s(x // 2 - 1))) % 1000000007
        else:
            fib_data[x] = (f_s(x // 2 + 1) ** 2 + f_s(x // 2) ** 2) % 1000000007
            return (f_s(x // 2 + 1) ** 2 + f_s(x // 2) ** 2) % 1000000007
n = int(input())
print(f_s((n // 2) * 2 + 1) - 1)