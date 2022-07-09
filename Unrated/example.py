N, M = map(int, input().split())
t1 = []
t2 = []

for _ in range(N):
    t1_line = list(input())
    t1.append(t1_line)
blank = input()
for _ in range(N):
    t2_line = list(input())
    t2.append(t2_line)
    
res = 0
for i in range(N):
    for j in range(M):
        if t1[i][j] == t2[i][j]:
            res += 1
print(res)
