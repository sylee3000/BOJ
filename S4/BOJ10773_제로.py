K = int(input())
remain_list = []
for i in range(K):
    n = int(input())
    if n != 0:
        remain_list.append(n)
    else:
        remain_list.pop()
print(sum(remain_list))