A, B, C = map(int, input().split())
res = 3
two_s = [2, 4, 8, 16, 32, 64]
if (B // A) == (B / A):
    for a in range(-100, 101):
        for b in range(-100, 101):
            if a + b == -(B / A) and a * b == (C / A):
                if a == b:
                    res = 3
                elif a in two_s and b in two_s:
                    res = 1
                else:
                    res = 2
print('이수근' if res == 1 else '정수근' if res == 2 else '둘다틀렸근')