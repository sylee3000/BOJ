from collections import deque
import math

min, max = map(int, input().split())
count = max - min + 1
d = [False] * (count)
max_sqrt = math.ceil(math.sqrt(max))


for i in range(2, max_sqrt + 1):
    a = (i ** 2) * (min // (i ** 2))
    while a <= max:
        if a >= min and d[a-min] == False:
            d[a-min] = True
            count -= 1
        a += i ** 2
    
print(count) 