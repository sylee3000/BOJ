import heapq
keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

N = int(input())
pos = {}
for _ in range(N):
    string = input()
    length = len(string)
    for i in string:
        if i not in pos.keys():
            pos[i] = 36 ** (length - 1)
        else:
            pos[i] += 36 ** (length - 1)
        length -= 1
h = []
for key, value in pos.items():
    key_value = keys.index(key)
    z_val = 35 * value
    formal_val = key_value * value
    diff = z_val - formal_val
    heapq.heappush(h, (-diff, z_val, formal_val))

k = int(input())
res = 0
while h:
    diff, z_val, formal_val = heapq.heappop(h)
    if k > 0:
        res += z_val
        k -= 1
    else:
        res += formal_val

res_for_36 = []
if res == 0:
    print(0)
else:
    while res > 0:
        res_for_36.append(keys[res % 36])
        res = res // 36
    print(*res_for_36[::-1], sep = '')