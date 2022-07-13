T = int(input())
for _ in range(T):
    k, u = input().split()
    if u == 'kg':
        mul = 2.2046
        ans_u = 'lb'
    elif u == 'lb':
        mul = 0.4536
        ans_u = 'kg'
    elif u == 'l':
        mul = 0.2642
        ans_u = 'g'
    elif u == 'g':
        mul = 3.7854
        ans_u = 'l'
    ans_k = round(float(k) * mul, 4)

    print(f'{ans_k:.4f} {ans_u}')