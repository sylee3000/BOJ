T = int(input())
for _ in range(T):
    Y, K = 0, 0
    for _ in range(9):
        y_point, k_point = map(int, input().split())
        Y += y_point
        K += k_point
    print("Yonsei" if Y > K else "Korea" if Y < K else "Draw")