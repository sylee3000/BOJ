from collections import deque
import math

G = int(input())
res = deque()

if G % 2 == 1 and G > 1:
    A = (G+1) // 2
    res.appendleft(A)
    A -= 1
else:
    A = G // 2 + 1
B = A - 1

while A >= math.sqrt(G) and B > 0:
    if (A ** 2 - B ** 2) == G:
        if A not in res:
            res.appendleft(A)
        A -= 1
    elif (A ** 2 - B ** 2) < G:
        B -= 1
    else:
        A -= 1

if res:
    for i in res:
        print(i)
else:
    print(-1)