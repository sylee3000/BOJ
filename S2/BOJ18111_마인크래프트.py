N, M, B = map(int, input().split())
minecraft = []
target_height = -1
total_time = 1e9
for _ in range(N):
    input_list = list(map(int, input().split()))
    minecraft = minecraft + input_list
max_height = max(minecraft)
min_height = min(minecraft)

for i in range(min_height, max_height + 1):
    remove_block = 0
    fill_block = 0
    for j in minecraft:
        if j > i:
            remove_block += j - i
        else:
            fill_block += i - j
    if fill_block > B + remove_block:
        continue
    case_time = 2 * remove_block + fill_block
    if total_time >= case_time:
        total_time = case_time
        target_height = i

print(total_time, target_height, sep=' ')

## PyPy3으로 제출