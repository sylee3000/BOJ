N = int(input())
list = [x for x in map(int, input().split())]
list_to_set = sorted(set(list))
set_to_dict = {}
for i in range(len(list_to_set)):
    set_to_dict[list_to_set[i]] = i
for i in list:
    print(set_to_dict[i], end=' ')