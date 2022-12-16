from collections import deque
import sys
input = sys.stdin.readline

input_list = deque(input().split())
n = int(input_list.popleft())
res_list = []
for i in input_list:
    res_list.append(int(i[::-1]))
while len(res_list) < n:
    add_list = input().split()
    for i in add_list:
        res_list.append(int(i[::-1]))
res_list.sort()
for i in res_list:
    print(i)