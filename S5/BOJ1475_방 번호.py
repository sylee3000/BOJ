import math

N = input()
number_list = [0] * 10
for i in N:
    number_list[int(i)] += 1
number_list[6] = math.ceil((number_list[6] + number_list[9]) / 2)
number_list[9] = 0
print(max(number_list))