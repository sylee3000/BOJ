T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    total_hak = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total += C * G
        total_hak += C
    print(int(total_hak), round(total / total_hak, 1))