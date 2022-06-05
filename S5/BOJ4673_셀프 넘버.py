def d(n):
    n_s = str(n)
    result = n
    for i in n_s:
        result += int(i)
    return result

list = [x for x in range(1, 10001)]
for i in range(1, 10001):
    if d(i) in list:
        list.remove(d(i))
for i in list:
    print(i)