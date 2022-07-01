import math
count = 0
while True:
    count += 1
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print(f'Triangle #{count}')
    if a == -1:
        if b < c:
            print(f'a = {math.sqrt(c ** 2 - b ** 2):.3f}')
        else:
            print('Impossible.')
    elif b == -1:
        if a < c:
            print(f'b = {math.sqrt(c ** 2 - a ** 2):.3f}')
        else:
            print('Impossible.')
    else:
        print(f'c = {math.sqrt(a ** 2 + b ** 2):.3f}')
    print()