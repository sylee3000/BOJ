from collections import deque

N, K = map(int, input().split())
num = deque(map(int, str(input())))

t = K
temp = deque()
while t > 0 and num:
    a = num.popleft()
    if not temp:
        temp.append(a)
    else:
        while temp and t > 0:
            last = temp.pop()
            if last >= a:
                temp.append(last)
                if len(temp) + 1 <= N-K:
                    temp.append(a)
                break
            else:
                t -= 1
        else:
            temp.append(a)
                
res = temp + num
print(*res, sep='')