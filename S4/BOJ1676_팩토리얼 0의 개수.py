N = int(input())
in_5 = 0
for i in range(1, N + 1):
    a = i
    while a >= 5:
        if a % 5 == 0:
            in_5 += 1
            a = a // 5
        else:
            break
print(in_5)