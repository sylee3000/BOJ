from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    count = int(input())
    numbers = input()[1:-1].strip("]").split(',')
    if count == 0:
        num_queue = []
    else:
        num_queue = deque(numbers)
    is_reversed = False
    for command in p:
        if command == 'R':
            is_reversed = is_reversed ^ True
        elif command == 'D':
            if count < 1:
                print("error")
                count = -1
                break
            elif is_reversed:
                num_queue.pop()
            else:
                num_queue.popleft()
            count -= 1
    if is_reversed:
        num_queue.reverse()
    if count >= 0:
        print("[" + ",".join(num_queue) + "]")