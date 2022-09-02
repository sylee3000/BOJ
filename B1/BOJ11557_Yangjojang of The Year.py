T = int(input())
for _ in range(T):
    alc = {}
    N = int(input())
    for _ in range(N):
        school, amount = input().split()
        alc[int(amount)] = school
    print(alc[max(alc.keys())])