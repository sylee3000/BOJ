N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
for i in info:
    grade = 1
    for j in info:
        if info.index(i) != info.index(j) and i[0]<j[0] and i[1]<j[1]:
            grade += 1
    print(grade, end=' ')