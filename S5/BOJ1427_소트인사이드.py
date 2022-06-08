N = input()
number_list = []
for i in N:
    number_list.append(i)
number_list.sort(reverse=True)
print(*number_list, sep='')