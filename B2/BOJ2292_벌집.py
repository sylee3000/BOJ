N = int(input())
k = N - 1
len = 1
while k > 0:
    k -= 6 * len
    len += 1
print(len)