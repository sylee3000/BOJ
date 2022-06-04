import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    op = input().split()
    
    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif op[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])