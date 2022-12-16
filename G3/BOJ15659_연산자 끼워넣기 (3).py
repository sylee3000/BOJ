from collections import deque
max_res, min_res = int(-1e9), int(1e9)

def cal(s, A, plus, minus, mul, div):
    if not A:
        global max_res, min_res
        res_part = sum(s)
        max_res = max(max_res, res_part)
        min_res = min(min_res, res_part)
        return
    else:
        if plus > 0:
            num = A.popleft()
            s.append(num)
            cal(s, A, plus - 1, minus, mul, div)
            s.pop()
            A.appendleft(num)
        if minus > 0:
            num = A.popleft()
            s.append(-num)
            cal(s, A, plus, minus - 1, mul, div)
            s.pop()
            A.appendleft(num)
        if mul > 0:
            if s:
                num = A.popleft()
                k = s.pop()
                s.append(num * k)
                cal(s, A, plus, minus, mul - 1, div)
                s.pop()
                s.append(k)
                A.appendleft(num)
        if div > 0:
            if s:
                num = A.popleft()
                k = s.pop()
                if k >= 0:
                    s.append(k // num)
                else:
                    s.append(-(abs(k) // num))
                cal(s, A, plus, minus, mul, div - 1)
                s.pop()
                s.append(k)
                A.appendleft(num)

N = int(input())
A = deque(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
s = []
s.append(A.popleft())
cal(s, A, plus, minus, mul, div)

print(max_res)
print(min_res)