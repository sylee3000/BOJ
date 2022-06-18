import sys
input = sys.stdin.readline

N = int(input())
std_num = []
for _ in range(N):
    std_num.append(input().replace('\n',''))
result = 0
point = std_num[0]
for i in range(len(point), 0, -1):
    key = []
    result += 1
    for j in range(N):
        key.append(std_num[j][i-1:])
    if len(set(key)) == N:
        print(result)
        break