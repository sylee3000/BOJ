N = int(input())
stairs_score = []
for i in range(N):
    stairs_score.append(int(input()))
max_score = {0:0, 1:stairs_score[0]}
def stair_game(N):
    if N > 1:
        max_score[2] = stairs_score[0] + stairs_score[1]
    if N > 2:
        max_score[3] = max(stairs_score[0] + stairs_score[2], stairs_score[1] + stairs_score[2])
    if N > 3:
        for i in range(4, N + 1):
            max_score[i] = max(max_score[i-2], max_score[i-3]+stairs_score[i-2])+stairs_score[i-1]
    return max_score[N]
print(stair_game(N))