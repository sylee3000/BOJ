alpha = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    max_alpha = 0
    for i in s:
        for j in range(len(alpha)):
            if alpha[j] == i:
                if max_alpha < j:
                    max_alpha = j
    print(max_alpha + 1)