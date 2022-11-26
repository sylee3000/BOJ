N = int(input())
dance = ['ChongChong']
for _ in range(N):
    A, B = input().split()
    if A in dance and B not in dance:
        dance.append(B)
    elif B in dance and A not in dance:
        dance.append(A)
print(len(dance))