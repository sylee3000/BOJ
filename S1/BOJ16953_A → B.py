A, B = map(int, input().split())
steps = 1
changed_B = B
while A < changed_B:
    if changed_B % 2 == 0:
        changed_B = changed_B / 2
        steps += 1
    elif changed_B % 10 == 1:
        changed_B = changed_B // 10
        steps += 1
    else:
        break
if A != changed_B:
    steps = -1
print(steps)
