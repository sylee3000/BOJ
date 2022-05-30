N = int(input())
number_list = list(map(int, input().split()))
result_num = number_list.pop()
total_case = [{number_list.pop(0):1}]
for i in number_list:
    case_list = {}
    for key, value in total_case[-1].items():
        if key + i <= 20:
            if not key + i in case_list.keys():
                case_list[key + i] = value
            else:
                case_list[key + i] += value
        if key - i >= 0:
            if not key - i in case_list.keys():
                case_list[key - i] = value
            else:
                case_list[key - i] += value
    total_case.append(case_list)
print(total_case[-1][result_num])