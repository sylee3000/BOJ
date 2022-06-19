N = int(input())

P_R = []
P_G = []
P_B = []

for i in range(N):
    R, G, B = map(int, input().split())
    if i == 0:
        P_R.append(R)
        P_G.append(G)
        P_B.append(B)
    else:
        P_R.append(min(P_G[i-1], P_B[i-1]) + R)
        P_G.append(min(P_R[i-1], P_B[i-1]) + G)
        P_B.append(min(P_G[i-1], P_R[i-1]) + B)
print(min(P_R[N-1], P_G[N-1], P_B[N-1]))