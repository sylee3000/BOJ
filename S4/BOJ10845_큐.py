import sys
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    op = input().split()
    
    if op[0] == 'push':
        queue.append(op[1])
    elif op[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif op[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])