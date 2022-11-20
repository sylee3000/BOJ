S = list(input())
count_0, count_1 = 0, 0
for i in range(len(S)):
    if S[i] == '0':
        count_0 += 1
    else:
        count_1 += 1
count_0, count_1 = count_0 // 2, count_1 // 2

new_S = []
for i in range(len(S)):
    if S[i] == '0':
        if count_0 > 0:
            count_0 -= 1
            new_S.append(S[i])
    else:
        new_S.append(S[i])

S = new_S[::-1]
new_S = []
for i in range(len(S)):
    if S[i] == '1':
        if count_1 > 0:
            count_1 -= 1
            new_S.append(S[i])
    else:
        new_S.append(S[i])
S = new_S[::-1]
print(*S, sep='')