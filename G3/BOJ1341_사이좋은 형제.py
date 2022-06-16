a, b = map(int, input().split())
n = 2
if b == 1:
    print('-' if a == 0 else '*')
else:
    while n <= 60:
        if (2 ** n - 1) % b == 0:
            result = a * ((2 ** n - 1) // b)
            break
        else:
            n += 1
    if n > 60:
        print(-1)
    else:
        result = bin(result)[2:]
        if n > len(result):
            result = '0'*(n-len(result)) + result
        for i in result:
            print('-' if i == '0' else '*', end='')