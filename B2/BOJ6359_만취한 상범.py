T = int(input())
for _ in range(T):
    n = int(input())
    room = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if room[j] == 0:
                room[j] = 1
            else:
                room[j] = 0
    print(sum(room))