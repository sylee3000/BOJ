import sys
input = sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    op = input().split()
    
    if op[0] == 'push_front':
        deque.insert(0, op[1])
    elif op[0] == 'push_back':
        deque.append(op[1])
    elif op[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.pop(0))
    elif op[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif op[0] == 'size':
        print(len(deque))
    elif op[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif op[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])