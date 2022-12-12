def fold(s, e, line):
    if abs(s - e) == 2:
        if line[s] == line[e]:
            return False
        else:
            return True
    else:
        mid = (s + e) // 2
        if fold(s, mid - 1, line) and fold(mid + 1, e, line):
            res = True
            for i in range(mid - s):
                if line[s + i] == line[e - i]:
                    res = False
            return res
        else:
            return False

T = int(input())
for _ in range(T):
    line = input()
    if len(line) == 1:
        print('YES')
    elif fold(0, len(line) - 1, line):
        print('YES')
    else:
        print('NO')