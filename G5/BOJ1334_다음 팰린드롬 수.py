import math

N = int(input())

if math.log10(N + 1) == int(math.log10(N + 1)):
    print(N + 2)
elif len(str(N)) == 1:
    print(N + 1)
else:
    left = int(str(N)[:len(str(N)) // 2])
    right = int(str(N)[(len(str(N)) + 1) // 2:])
    if int(str(left)[::-1]) <= right:
        if len(str(N)) % 2 == 0:
            print(int(str(left+1) + str(left+1)[::-1]))
        elif int(str(N)[len(str(N)) // 2]) == 9:
            print(int(str(left+1) + str(0) + str(left+1)[::-1]))
        else:
            print(int(str(left) + str(int(str(N)[len(str(N)) // 2])+1) + str(left)[::-1]))
    else:
        if len(str(N)) % 2 == 0:
            print(int(str(left) + str(left)[::-1]))
        else:
            print(int(str(left) + str(N)[len(str(N)) // 2] + str(left)[::-1]))