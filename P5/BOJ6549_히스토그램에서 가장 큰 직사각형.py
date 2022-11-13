import sys
from collections import deque
input = sys.stdin.readline

while True:
    lst = deque(map(int, input().split()))
    n = lst.popleft()
    if n == 0:
        break
    res = 0
    stack = []
    index = 0
    
    for i in lst:
        l_index = index
        last_index = 0
        if not stack:
            stack.append((i, index))
            index += 1
        else:
            while True:
                if not stack:
                    stack.append((i, last_index))
                    index += 1
                    break
                last_h, last_index = stack.pop()
                if last_h < i:
                    stack.append((last_h, last_index))
                    stack.append((i, l_index))
                    index += 1
                    break
                elif last_h == i:
                    stack.append((last_h, last_index))
                    index += 1
                    break
                else:
                    res = max(res, last_h * (index - last_index))
                    l_index = last_index
    while stack:
        h, i = stack.pop()
        res = max(res, h * (n - i))
    print(res)