import sys
input = sys.stdin.readline

M = int(input())
S = []
for i in range(M):
    order = input().split()
    command = order[0]
    if command == 'add':
        if int(order[1]) not in S:
            S.append(int(order[1]))
    elif command == 'remove':
        if int(order[1]) in S:
            S.remove(int(order[1]))
    elif command == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.append(int(order[1]))
    elif command == 'all':
        S = [x for x in range(1,21)]
    elif command == 'empty':
        S = []