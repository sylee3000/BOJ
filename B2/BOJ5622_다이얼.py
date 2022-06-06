dial_num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
ans = 0
for i in word:
    for j in dial_num:
        if i in j:
            ans += dial_num.index(j) + 3
print(ans)