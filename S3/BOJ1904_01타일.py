N = int(input())

tiles_01 = [0, 1, 2]

if N >= 3:
    for i in range(3, N + 1):
        tiles_01.append((tiles_01[i-2] + tiles_01[i-1]) % 15746) 
print(tiles_01[N])