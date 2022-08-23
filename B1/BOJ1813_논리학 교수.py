N = int(input())
lst = list(map(int, input().split()))
dict = {0: 0}
for i in lst:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1

res = -1

for i in dict.keys():
    if dict[i] == i:
        res = max(res, i)
        
print(res)