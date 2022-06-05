T = int(input())
list = [1, 1, 2, 4]
for _ in range(T):
    n = int(input())
    if n >= len(list):
        for i in range(len(list), n + 1):
            list.append(list[i-1] * 2 - list[i-4])
    print(list[n])