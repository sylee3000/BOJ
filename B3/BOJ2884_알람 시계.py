H, M = map(int, input().split())
if M < 45:
    changed_M = M + 15
    changed_H = (H - 1) % 24
else:
    changed_M = M - 45
    changed_H = H
print(changed_H, changed_M)