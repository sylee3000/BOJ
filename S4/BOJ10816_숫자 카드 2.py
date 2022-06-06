import sys
input = sys.stdin.readline

N = int(input())
card_list = [x for x in map(int, input().split())]
card_dict = {}
for i in card_list:
    if i in card_dict.keys():
        card_dict[i] += 1
    else:
        card_dict[i] = 1

M = int(input())
q_list = [x for x in map(int, input().split())]

for i in q_list:
    if i in card_dict.keys():
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')