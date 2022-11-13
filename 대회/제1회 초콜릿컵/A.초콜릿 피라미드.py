import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    white, cnt = 0, 0
    temp = R * C
    white += temp
    while R > 0 and C > 0:
        R -= 1
        C -= 1
        temp = R * C
        white += 2 * temp
        cnt += 1
    white -= temp
    print(white, white - cnt)