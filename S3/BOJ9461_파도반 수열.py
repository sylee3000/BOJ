T = int(input())
wave_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
def wave(N):
    if N <= len(wave_list):
        return wave_list[N-1]
    else:
        for i in range(len(wave_list) + 1, N + 1):
            wave_list.append(wave_list[i-6] + wave_list[i - 2])
        return wave_list[N - 1]
for i in range(T):
    print(wave(int(input())))