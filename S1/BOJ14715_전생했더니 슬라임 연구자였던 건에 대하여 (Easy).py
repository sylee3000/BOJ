import math

K = int(input())

i = 2
count = 0
while K >= i:
    if K % i == 0:
        K = K // i
        count += 1
    else:
        i += 1
print(math.ceil(math.log2(count)))