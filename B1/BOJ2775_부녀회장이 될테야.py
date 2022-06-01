T = int(input())
room = [[x for x in range(1, 15)]]
for i in range(1, 15):
    floor_list = []
    for j in range(14):
        floor_list.append(sum(room[i-1][:j+1]))
    room.append(floor_list)
for _ in range(T):
    K = int(input())
    N = int(input())
    print(room[K][N-1])