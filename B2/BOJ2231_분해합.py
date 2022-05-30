N = int(input())
result = 0
while result < N:
    a = result
    sum = a
    while a > 0:
        sum += a % 10
        a = a // 10
    if sum == N:
        print(result)
        break
    else:
        result += 1
if result == N:
    print(0)