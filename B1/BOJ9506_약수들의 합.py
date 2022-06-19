while True:
    n = int(input())
    if n == -1:
        break
    div = []
    i = 1
    while i < n:
        if n % i == 0 :
            div.append(i)
        i += 1
    if n == sum(div):
        print(f'{n} = ', end = '')
        print(*div, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')