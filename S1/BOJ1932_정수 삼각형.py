n = int(input())
sum_list = []
for i in range(n):
    if i == 0:
        sum_list.append(int(input()))
        continue
    line_num_list = list(map(int, input().split()))
    line_sum_list = []
    for j in range(i + 1):
        if j == 0:
            line_sum_list.append(sum_list[0] + line_num_list[j])
        elif j == i:
            line_sum_list.append(sum_list[-1] + line_num_list[j])
        else:
            line_sum_list.append(max(sum_list[j-1], sum_list[j]) + line_num_list[j])
    sum_list = line_sum_list
print(max(sum_list))