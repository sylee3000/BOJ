T = int(input())
room_number = []
for i in range(T):
    H, W, N = map(int, input().split(' '))
    room_number.append((((N - 1) % H) + 1) * 100 + ((N - 1) // H) + 1)

for i in room_number:
    print(i)